import markdown
from markdown.extensions.codehilite import CodeHiliteExtension
from markdown.extensions.toc import TocExtension


def convert_markdown_to_html(input_file, output_file, css_file=None):
    """
    将 Markdown 文件转换为完整的 HTML 文件

    Args:
        input_file: 输入的 Markdown 文件路径
        output_file: 输出的 HTML 文件路径
        css_file: 可选的 CSS 样式文件路径
    """
    # 读取 Markdown
    with open(input_file, 'r', encoding='utf-8') as f:
        md_text = f.read()

    # 配置扩展
    extensions = [
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc',
        'markdown.extensions.tables',
        'markdown.extensions.fenced_code',
        'markdown.extensions.admonition',
    ]

    # 转换为 HTML
    html_content = markdown.markdown(
        md_text,
        extensions=extensions,
        extension_configs={
            'markdown.extensions.codehilite': {
                'css_class': 'codehilite',
                'linenums': True,  # 显示行号
            },
            'markdown.extensions.toc': {
                'title': '目录',
                'anchorlink': True,  # 标题添加链接
            }
        }
    )

    # 创建完整的 HTML 文档
    html_template = f"""
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{input_file} - Markdown 转换</title>
    <style>
        /* 默认样式 */
        body {{
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
            line-height: 1.6;
            color: #24292e;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f6f8fa;
        }}

        h1, h2, h3, h4, h5, h6 {{
            margin-top: 24px;
            margin-bottom: 16px;
            font-weight: 600;
            line-height: 1.25;
        }}

        h1 {{ border-bottom: 2px solid #eaecef; padding-bottom: 0.3em; }}
        h2 {{ border-bottom: 1px solid #eaecef; padding-bottom: 0.3em; }}

        code {{
            padding: 0.2em 0.4em;
            margin: 0;
            font-size: 85%;
            background-color: rgba(27,31,35,0.05);
            border-radius: 3px;
            font-family: "SFMono-Regular", Consolas, "Liberation Mono", Menlo, Courier, monospace;
        }}

        pre {{
            background-color: #f6f8fa;
            border-radius: 3px;
            padding: 16px;
            overflow: auto;
        }}

        blockquote {{
            padding: 0 1em;
            color: #6a737d;
            border-left: 0.25em solid #dfe2e5;
            margin: 0;
        }}

        table {{
            border-spacing: 0;
            border-collapse: collapse;
            display: block;
            width: 100%;
            overflow: auto;
        }}

        th, td {{
            padding: 6px 13px;
            border: 1px solid #dfe2e5;
        }}

        th {{
            font-weight: 600;
            background-color: #f6f8fa;
        }}

        a {{
            color: #0366d6;
            text-decoration: none;
        }}

        a:hover {{
            text-decoration: underline;
        }}

        img {{
            max-width: 100%;
            box-sizing: border-box;
        }}

        /* 代码高亮样式 */
        .codehilite .hll {{ background-color: #ffffcc }}
        .codehilite .c {{ color: #999988; font-style: italic }}
        .codehilite .err {{ color: #a61717; background-color: #e3d2d2 }}
        .codehilite .k {{ color: #000000; font-weight: bold }}
        /* 更多 Pygments 样式... */

        /* 响应式设计 */
        @media (max-width: 768px) {{
            body {{
                padding: 10px;
            }}
        }}
    </style>

    <!-- 可选的额外 CSS -->
    {f'<link rel="stylesheet" href="{css_file}">' if css_file else ''}

    <!-- 代码高亮样式（可选） -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.8.0/styles/github.min.css">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.8.0/highlight.min.js"></script>
    <script>hljs.highlightAll();</script>
</head>
<body>
    <div class="markdown-body">
        {html_content}
    </div>

    <script>
        // 自动为表格添加样式
        document.addEventListener('DOMContentLoaded', function() {{
            // 为所有表格添加 responsive 类
            const tables = document.querySelectorAll('table');
            tables.forEach(table => {{
                const wrapper = document.createElement('div');
                wrapper.className = 'table-responsive';
                table.parentNode.insertBefore(wrapper, table);
                wrapper.appendChild(table);
            }});

            // 为新窗口打开的链接添加图标
            const links = document.querySelectorAll('a[href^="http"]');
            links.forEach(link => {{
                if (link.hostname !== window.location.hostname) {{
                    link.target = '_blank';
                    link.innerHTML += ' ↗';
                }}
            }});
        }});
    </script>
</body>
</html>
    """

    # 写入文件
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html_template)

    print(f"转换完成！输出文件: {output_file}")

# 使用示例
# if __name__ == "__main__":
#     convert_markdown_to_html("report_20260118 (2).md", "report_20260118 (2).html")

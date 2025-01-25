
import argparse
import json
import os

def jsontohtml(ifile):
    for filename in os.listdir(ifile):
        if not filename.endswith(".json"):
            print('isnot','--', filename)
            continue
        else:
            html_content = """
            <!DOCTYPE html>
            <html lang="fr">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Messages Dynamiques</title>
                <style>
                    body {
                        font-family: 'Arial', sans-serif;
                        background-color: #f4f4f4;
                        color: #333;
                        margin: 0;
                        padding: 0;
                    }
                    h1 {
                        text-align: center;
                        margin-top: 20px;
                        color: #4CAF50;
                    }
                    .message {
                        background-color: #fff;
                        border: 1px solid #ddd;
                        border-radius: 8px;
                        margin: 15px auto;
                        padding: 15px;
                        max-width: 800px;
                        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                        transition: transform 0.3s ease;
                    }
                    .message:hover {
                        transform: scale(1.02);
                    }
                    .message img {
                        width: 50px;
                        height: 50px;
                        border-radius: 50%;
                        margin-right: 15px;
                    }
                    .message-content {
                        line-height: 1.6;
                    }
                    .author-name {
                        font-weight: bold;
                        color: #007BFF;
                    }
                    .timestamp {
                        color: #777;
                        font-size: 12px;
                        margin-top: 5px;
                    }
                    .message-footer {
                        margin-top: 10px;
                        font-size: 14px;
                        color: #555;
                    }
                    .attachment img {
                        width: 100%; 
                        max-width: 800px; 
                        height: auto; 
                        border-radius: 8px;
                        margin-top: 10px;
                        display: block;
                        margin-left: auto;
                        margin-right: auto;
                    }
                </style>
            </head>
            <body>
                <h1>Messages Dynamiques</h1>
            """
            
            
            
            
            
            
            
            
            with open(os.path.join(ifile,filename), "r", encoding="utf-8") as files:
                data = json.load(files)

            messages = data.get("messages", [])
            for message in messages:
                messid = message.get("id")
                cont = message.get("content")
                author = message.get("author")
                
                name = author.get("name")
                avatar = author.get("avatarUrl")
                timestamp = message.get("timestamp")
                html_content += f"""
                <div class="message">
                    <img src="{avatar}" alt="Avatar de {name}">
                    <div class="message-content">
                        <div class="author-name">{name}</div>
                        <div>{cont}</div>
                        <div class="timestamp">{timestamp}</div>
                """

                attachments = message.get("attachments", [])
                if attachments:
                    for attachment in attachments:
                        attachment_url = attachment.get("url")
                        html_content += f"""
                        <div class="attachment">
                            <img src="{attachment_url}" alt="Attachment Image">
                        </div>
                        """
                
                html_content += """
                </div>
                </div>
                """

            html_content += """
            </body>
            </html>
            """

            with open(filename+".html", "w", encoding="utf-8") as file:
                file.write(html_content)

            print("Done")


def main():
    prs = argparse.ArgumentParser(description="Convert Discord message logs (exported as JSON files) into beautifully formatted HTML pages. Simply provide the path(s) to your JSON file(s) — you can process one or multiple files at once.")
    prs.add_argument("--input", required = False, help="Json File Path")
    args = prs.parse_args()
    
    if args.input:
        jsontohtml(args.input)
    else:
        ipath = input("Directory path: ")
        ipath = ipath.replace(os.path.sep, "/")
        jsontohtml(ipath)
    
if __name__ == '__main__':
    main()
    os.system("pause")

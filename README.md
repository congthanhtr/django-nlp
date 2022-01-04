# Build a syntactic tree in natural language processing for English and Vietnamese.
In this project, we, contributors, are making a website to parse a sentence in English or Vietnamese into a syntactic tree using machine learning, not rule-based method or deep learning
## Contributors
- *19120659_Phạm Văn Thành*
- *19120660_Trương Công Thành*
- *19120667_Nguyễn Văn Thịnh*
## Project Structure
### NLP_SYNTACTIC_TREE
  &emsp;-model\
    &emsp;&emsp;--english        : source code to train pos tagging and chunker model for English\
    &emsp;&emsp;--vietnamese     : source code to train pos tagging and chunker model for Vietnamese\
    &emsp;&emsp;--test.py        : test parsing an English sentence into a tree by using our own pre trained model\
    &emsp;&emsp;--vietnamese_test: test parsing a Vietnamese sentence into a tree by using our own pre trained model\
  &emsp;-nlp_syntactic_tree: some settings for website\
  &emsp;-static/assets: all css/javascript files used in this project\
  &emsp;-template: all html files\
  &emsp;-tree:\
  &emsp;&emsp;--urls.py: define link route\
  &emsp;&emsp;--views.py: implement function to process parsing then send data to template\
  &emsp;-manage.py: run admin task\
## How to use
1. Clone this repo
2. install requirements file: `pip install -r requirements.txt`
3. Open cmd at: .../nlp_syntactic_tree/ and run command :`python manage.py runserver`
4. Ctrl + click to follow link or open your web browser and start the server at: http://127.0.0.1:8000/
5. Test our website
## Referenec
1.Vietnamese training corpus source: https://github.com/lupanh/vTools/tree/master/data
2. https://www.amazon.com/Python-Text-Processing-NLTK-Cookbook/dp/1782167854

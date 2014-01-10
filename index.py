import crawler
from flask import Flask,redirect,request
import markup
from ConfigParser import SafeConfigParser

app = Flask(__name__)

@app.route('/user/<int:userid>')
def show_user_profile(userid):
    return 'User id %d' % userid

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        app.logger.debug(request.form['f1'])
        app.logger.debug(request.form['f2'])
        f1 = request.args.get('f1','no f1')
        f2 = request.args.get('f2','no f2')
        app.logger.debug(f1)
        app.logger.debug(f2)
        return "Done upload\n"

@app.route("/")
def hello():
    parser = SafeConfigParser()
    parser.read('crawler.conf')
    '''
    page = markup.page()
    page.init( title="Search Result",                           
               charset="utf-8",
               header="",
               footer="" )
    page.p(u"==================================================")
    page.p(u"Done")
    page.a(u"Link",class_='internal',href="http://localhost/a.html")
    page.p(u"==================================================")
    '''
    a=crawler.audio_crawler()
    page=a.gen_html(pages=parser.getint('core', 'pages'),web_root=parser.get('core', 'web_root'))
    return page
#    return page.get_result()

if __name__ == "__main__":
    app.run(debug=True)

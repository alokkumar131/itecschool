from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/', methods=['GET'])
def main():
    return render_template('index.html')

# @app.before_request
# def before_request():
#     # If the request is sicure it should already be https, so no need to redirect
#     if not request.is_secure:
#         currentUrl = request.url
#         print(currentUrl)
#         if currentUrl.startswith('http://'):
#             # http://itecschool.com -> https://itecschool.com
#             # http://www.itecschool.com -> https://www.itecschool.com
#             redirectUrl = currentUrl.replace('http://', 'https://', 1)
#         elif currentUrl.startswith('www'):
#             # Here we redirect the case in which the user access the site without typing any http or https
#             # www.example.com -> https://www.itecschool.com
#             redirectUrl = currentUrl.replace('www', 'https://www', 1)
#         else:
#             # I do not now when this may happen, just for safety
#             redirectUrl = 'https://www.itecschool.com'
#         code = 301
#         return redirect(redirectUrl, code=code)

if __name__ == '__main__':
    app.run(debug=True)
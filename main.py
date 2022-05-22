from website import create_app

app = create_app

if __name__ == '__main__':
    app.run(debug=True)'''只有在我们run这个文件的而不是导入文件时才会执行以下'''
    '''run flask application start off a web server debug=true 只当我们改变code时会自动rerun web服务器'''

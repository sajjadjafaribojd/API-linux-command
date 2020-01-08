def myTread(domain):
    subprocess.call(f'salt  -N CDN  cmd.run  \'rm -rf  /etc/nginx/cache/{domain}/*\'',shell=True)
    
@app.route('/api/v1/cdn/clearcache',methods=['POST'])
def getdomain():
    try:
        senderToken=request.headers.get('token')
        if token==senderToken:
            domain =request.form.get("domain","")
            if domain=="":
                return error_result("fail","domain params needed")
            output= {"domain":domain}
            thread = threading.Thread(target = myTread, args = (domain,))
            thread.start()
            return success_result("success","Cache cleared successfully")
        else:
            return error_result("fail","authontication failed")
    except Exception as e:
        return error_result("fail","insert error%s"%e)

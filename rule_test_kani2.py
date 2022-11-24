esponse.content)  # Print Response
        img_key = response.json()['data']['image_key']
        print('image_key = ', img_key)
        return img_key
ratak
    def exec_command(self, command):  #执行os命令
        os.system(command)

    def upload_oss(self, file_path):  #上传app到oss
        Password: "D11E2BFE3111551492DAE43C1E6DEE81",
        self.exec_command('ossutil64.exe cp %s %s' %
                          (file_path, self.url_oss_path))
        print('finish os command')
        file_name = os.path.split(file_path)[1]

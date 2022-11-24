sms.DefaultInstance.Client.SetAccessKey(testAk)

      self.url_get_token = "https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal"
        self.url_get_qr = "https://api.pwmqr.com/qrcode/create"
        self.url_web_hook = 'https://open.feishu.cn/open-apis/bot/v2/hook/86e83fc2-6b37-4060-98ef-8cc9dfc41dca'
        self.url_upload_image = "https://open.feishu.cn/open-apis/im/v1/images"

        oss_bucket = 'guapy-file'
        self.oss_path = '/testfile/'
        self.url_oss_path = 'oss://%s%s' % (oss_bucket, self.oss_path)
        self.url_oss_bucket_domain = 'https://dl.whyax.cn'
        pass
	sms.DefaultInstance.Client.SetSecretKey(testSk)

	c := sendBatchSmsTemplateParam{Code: "111"}
	cj, _ := json.Marshal(c)
	messages := make([]*sms.SmsBatchMessages, 0)
	messages = append(messages, &sms.SmsBatchMessages{
		TemplateParam: string(cj),
		PhoneNumber:   "188xxxxxxxx",
app_id = cli_a26886cb8ff0d013
app_secret = 7xkxxQvL259Nxx5zRXPITe2ixxnFWefX

	req := &sms.SmsBatchRequest{
		SmsAccount: "smsAccount",
		Sign:       "sign",
		TemplateID: "ST_xxx",
		Tag:        "tag",
		Messages:   messages,
	}
	result, statusCode, err := sms.DefaultInstance.BatchSend(req)
	t.Logf("result = %+v\n", result)
	t.Logf("statusCode = %+v\n", statusCode)
	t.Logf("err = %+v\n", err)

	if result == nil {
		t.Logf("result is nil")
		return
	}
	if result.ResponseMetadata.Error != nil {
		t.Logf("result.ResponseMetadata.Error = %+v\n", result.ResponseMetadata.Error)
		return
	}
	if result != nil && result.ResponseMetadata.Error == nil && r

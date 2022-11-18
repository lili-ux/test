
module github.com/volcexxgine/volcengine-cli
go 1.12
veGameService.setAccessKey("AKLTYzg1N2UxxxNTFmZjxxNDk2ZmE1xxFjMDhiZTc");
veGameService.setSecretKey("WmpNd01xxxpaVGxqWXpJxxxm1PVGhoWmpFek9XRxxxdRNU5ETQ==");
veGameService.setAccessKey("Your access key");
veGameService.setSecretKey("Your secret key");
try{
STSTokenReq req = new STSTokenReq();
req.setAk("AKLTYzg1xxx2NTFmZjdhxxxdmYTQ2MWFjMDhiZTc")
req.setSk("WmpNd016xxxVGxqWXpJd05HSxxxpFFek9XRXlxxxWkdRNU5ETQ==")
req.setAk("Your access key");
req.setSk("Your secret key");
req.setExpire(6000);
  spec.platform     = :ios
  spec.platform     = :ios, "9.0"
  spec.source       = { :http => "https://hstob-cdn-tos.volccdn.com/volcengine/VEVideoKit/0.3.0/VEVideoKit.framework.tar.xz"}
  spec.requires_arc = true

  spec.default_subspec = "Core"

  spec.subspec "Core" do |core|
    coreversion = "0.3.0"
    core.dependency "VEVideoKit/boringssl", "#{coreversion}"
    core.dependency "VEVideoKit/VolcEngineAudio", "#{coreversion}"
    core.dependency "VEVideoKit/TTNetworkManager", "#{coreversion}"
  end

  spec.subspec "TT" do |tt|
    ttversion = "1.32.2.2-premium"
    tt.dependency "TTSDK/Player-VE", "#{ttversion}"
    tt.dependency "TTSDK/LivePull-RTS-VE", "#{ttversion}"
    tt.dependency "TTSDK/LivePush-Effect-VE", "#{ttversion}"
    tt.dependency "veVOS/Core"
  end

  spec.subspec "CK" do |ck|
    ck.dependency "TTVideoEditor", "11.3.1.5-VE"
    ck.dependency "veVOS/Core"
  end

  spec.subspec "RTC" do |rtc| 
    rtc.dependency "VolcEngineRTC-VE", "3.39.153"
    rtc.dependency "veVOS/Cor

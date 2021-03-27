from appium import webdriver


desired_caps={}
desired_caps['platformName']='Android'
desired_caps['platformVersion']='6.0'
desired_caps['deviceName']='emulator-5554'
desired_caps['appPackage']='com.tencent.mm'
desired_caps['appActivity']='com.tencent.mm.app.WeChatSplashActivity'
desired_caps['noReset']='True'
driver=webdriver.Remote("http://127,0,0,1:4723/wd/hub",desired_caps)



driver.quit()
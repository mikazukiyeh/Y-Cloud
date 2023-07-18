from selenium import webdriver
from selenium.webdriver.common.by import By

# 設定 ChromeDriver 路徑
chromedriver_path = '/Users/SCE/Downloads/chromedriver'

# 開啟 Chrome 瀏覽器
options = webdriver.ChromeOptions()
options.add_argument('incognito')  # 可以在無頭模式下執行
driver = webdriver.Chrome(options = options)

# 前往登入頁面
driver.get("https://eid.townway.com.tw/accounts/signin.html")

# 填寫登入資訊
username_input = driver.find_element(By.ID,'email')
password_input = driver.find_element(By.ID,'password')
username_input.send_keys("ntc@gmail.com")
password_input.send_keys("ntc#1234")

# 提交表單
result = driver.find_element(By.XPATH, '//button[@class="btn btn-block btn-primary"]')
result.submit()

# 等待登入完成
driver.implicitly_wait(10)

# 執行其他操作...
# 例如，確認是否登入成功，或執行其他操作。

# 關閉瀏覽器
driver.quit()

import json
import pickle
from os.path import exists

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()

driver.get("https://wap.showstart.com/pages/passport/login/login?redirect=%2Fpages%2FmyHome%2FmyHome")

wait = WebDriverWait(driver, 300, 0.3).until(EC.title_is(u"我的"))
#
local_storage = driver.execute_script("return window.localStorage")

print(local_storage)

pickle.dump(local_storage, open("local_storages.pkl", "wb"))

driver.quit()
import time
import os
from urllib.request import urlretrieve
from selenium import webdriver
folder = 2
num = 2
chromedriver = "C:/Users/KYC/Downloads/chromedriver_win32/chromedriver.exe"


options = webdriver.ChromeOptions()
options.add_argument("--headless")
driver = webdriver.Chrome(chromedriver, options=options)
print("+" * 100)
print("식재료 크롤링")
print("-" * 100)
driver.get("https://www.shutterstock.com/ko/search/%EC%96%91%ED%8C%8C?kw=%EB%AC%B4%EB%A3%8C+%EC%9D%B4%EB%AF%B8%EC%A7%80+%EC%82%AC%EC%9D%B4%ED%8A%B8&c3apidt=p16549324588&gclid=Cj0KCQiA1pyCBhCtARIsAHaY_5fh5HiVtKI_NGC3isKMj3QL700h_s-29pOxG9t-qaoI-L_a7uY3ZGkaAvJjEALw_wcB&gclsrc=aw.ds&image_type=photo&page="+str(num))
while num < 200:
    img_folder_path = "C:/Users/KYC/Downloads/onion/"+str(folder)
    if not os.path.isdir(img_folder_path):  # 없으면 새로 생성
        os.mkdir(img_folder_path)
    time.sleep(2)
    print(num,"페이지")


    ingredients = driver.find_elements_by_css_selector(
        "#content > div.s_f_ff6d0 > div > div.oc_ab_e5c9b.oc_ab_46972.b_Q_f0f29.oc_ab_6c502.b_Q_7113c.oc_ab_71c37.b_Q_dd576.oc_ab_4ae09.b_Q_045e8 > div.oc_ab_57b1b.b_Q_01b73 > main > div > div:nth-child(2) > div> div")
    # ingredients = title.find_elements_by_tag_name("div")
    print(len(ingredients))
    cnt = 0

    for item in ingredients:
        if(cnt > 0):
            url = item.find_element_by_tag_name(
                "div > a > img").get_attribute("src")
            if url is not None:
                start = url.rfind('.')
                end = url.rfind('')
                filetype = url[start:end]
                urlretrieve(url, 'C:/Users/KYC/Downloads/onion/' +
                            str(folder)+'/{}{}'.format(cnt, filetype))
        cnt += 1
    # nextpage = driver.find_element_by_css_selector("#content > div.s_f_ff6d0 > div > div.oc_ab_e5c9b.oc_ab_46972.b_Q_f0f29.oc_ab_6c502.b_Q_7113c.oc_ab_71c37.b_Q_dd576.oc_ab_4ae09.b_Q_045e8 > div.oc_ab_57b1b.b_Q_01b73 > main > div > div.z_b_39dd6.k_a_5828e.k_a_228d7 > div.k_a_48274.k_a_1841e.k_a_ab189.k_a_53dab > div > a")
    # nextpage = nextpage.get_attribute("href")
    # print(nextpage)
    num+=1
    folder+=1
    driver.get("https://www.shutterstock.com/ko/search/%EC%96%91%ED%8C%8C?kw=%EB%AC%B4%EB%A3%8C+%EC%9D%B4%EB%AF%B8%EC%A7%80+%EC%82%AC%EC%9D%B4%ED%8A%B8&c3apidt=p16549324588&gclid=Cj0KCQiA1pyCBhCtARIsAHaY_5fh5HiVtKI_NGC3isKMj3QL700h_s-29pOxG9t-qaoI-L_a7uY3ZGkaAvJjEALw_wcB&gclsrc=aw.ds&image_type=photo&page="+str(num))
driver.close()

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import ui
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from selenium.common.exceptions import NoSuchElementException
import requests
import time
import random

class instagramBot:
    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox()
        request = requests.get("https://www.instagram.com/duckcouncil/")
        soup = BeautifulSoup(request.content,"html.parser")
        following = soup.find("meta",property="og:description")
        content = following["content"]
        first_coma = content.index(",")
        start_index = content.index(",",first_coma+1)
        raw_output = content[start_index+1:20]

        if raw_output[0] == " ":
            self.complete_output = int(raw_output.strip())
        else:
            self.complete_output = int(raw_output)
    def login(self):
        self.driver.get("https://www.instagram.com/")
        time.sleep(10   )
        username_input = self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input")
        username_input.send_keys(self.username)
        time.sleep(10)
        password_input = self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input")
        password_input.send_keys(self.password)
        time.sleep(10)
        login_button = self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button")
        login_button.click()
        time.sleep(10)
        not_now = self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button")
        not_now.click()
        time.sleep(5)
        ui.WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".aOOlW.HoLwm"))).click()
        time.sleep(10)

    def autofollow(self,users,num):
        for i in range(len(users)):
            time.sleep(10)
            self.driver.get("https://www.instagram.com/"+users[i]) 
            followers = self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[2]/a")
            followers.click()
            time.sleep(20)
            for j in range(1,num):
                time.sleep(20)
                try: 
                    follow_button = self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div[2]/ul/div/li["+str(j)+"]/div/div[3]/button")
                    time.sleep(10)
                    follow_button.click()
                except NoSuchElementException:
                    follow_button = self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div[2]/ul/div/li["+str(j)+"]/div/div[2]/button")	
                    follow_button.click()
                try:
                    unFollow = self.driver.find_element_by_xpath("/html/body/div[5]/div/div/div/div[3]/button[1]")
                    unFollow.click()
                except NoSuchElementException:
                    continue
                time.sleep(20)
        time.sleep(10)
    def autoUnFollow(self):
        self.driver.get("https://www.instagram.com/"+self.username+"/")
        time.sleep(15)
        following_button = self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[3]/a")
        following_button.click()
        for i in range(1,self.complete_output+1):
            unfollow_button = self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div[2]/ul/div/li["+str(i)+"]/div/div[3]/button")
            unfollow_button.click()
            time.sleep(10)
    
    def autoSpamDm(self,message,num):
        for i in range(1,num):
            self.driver.get("https://www.instagram.com/"+self.username+"/")
            time.sleep(15)
            following_users = self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[3]/a")
            following_users.click()
            time.sleep(15)
            user = self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div[2]/ul/div/li["+str(i)+"]/div/div[2]/div[1]/div/div/span/a")
            user.click()
            time.sleep(10)
            dm_message = self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/div/div[1]/div/button")
            dm_message.click()
            time.sleep(10)
            input_message = self.driver.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea")
            input_message.send_keys(message)
            time.sleep(10)
            send_message = self.driver.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button")
            send_message.click()
            time.sleep(10)
    def autoLikingByFeed(self,num):
        self.driver.get("https://www.instagram.com/explore/")
        for i in range(1,num):
            time.sleep(10)
            post = self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div[1]/div/div[1]/div[3]")
            ActionChains(self.driver).move_to_element(post).click().perform() 
            time.sleep(15)
            like = self.driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/article/div[3]/section[1]/span[1]/button")
            like.click()
            time.sleep(10)
            next_post = self.driver.find_element_by_xpath("/html/body/div[4]/div[1]/div/div/a[2]")
            next_post.click()
            time.sleep(40)
    def autoLikingByHashtag(self,hashtag,num):
        for i in range(len(hashtag)):       
            self.driver.get("https://www.instagram.com/explore/tags/"+hashtag[i]+"/")
            post_ = self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[1]/div/div/div[1]/div[2]")
            ActionChains(self.driver).move_to_element(post_).click().perform()
            for j in range(0,num):
                time.sleep(10) 
                like1 = self.driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/article/div[3]/section[1]/span[1]/button")
                like1.click() 
                time.sleep(5) 
                next_post1 = self.driver.find_element_by_xpath("/html/body/div[4]/div[1]/div/div/a[2]")
                next_post1.click()
    def autoCommentingByFeed(self,comment,num):
        self.driver.get("https://www.instagram.com/explore/")
        for i in range(1,num):
            time.sleep(20)
            post = self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div[1]/div/div[1]/div[3]")
            ActionChains(self.driver).move_to_element(post).click().perform() 
            time.sleep(20)
            commento = self.driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/article/div[3]/section[1]/span[2]/button")
            commento.click()
            time.sleep(20)
            post_comment = self.driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/article/div[3]/section[3]/div/form/textarea")
            post_comment.send_keys(comment)
            time.sleep(30)
            post = self.driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/article/div[3]/section[3]/div/form/button")
            post.click()
            next_post = self.driver.find_element_by_xpath("/html/body/div[4]/div[1]/div/div/a[2]")
            next_post.click()
            time.sleep(10)
    def autoCommentingByHashtag(self,comment,hashtag,num):
        for i in range(len(hashtag)):
            self.driver.get("https://www.instagram.com/explore/tags/"+hashtag[i]+"/")
            time.sleep(10)
            post_ = self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[1]/div/div/div[1]/div[2]")
            ActionChains(self.driver).move_to_element(post_).click().perform()
            time.sleep(10)
            for j in range(0,num):
                try:
                    time.sleep(15) 
                    commento = self.driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/article/div[3]/section[1]/span[2]/button")
                    commento.click() 
                    time.sleep(5) 
                    commento_input = self.driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/article/div[3]/section[3]/div/form/textarea")
                    commento_input.send_keys(comment)
                    time.sleep(5)
                    post_comment = self.driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/article/div[3]/section[3]/div/form/button")
                    post_comment.click()
                except NoSuchElementException:
                    time.sleep(10)
                    continue
                
                time.sleep(5)
                next_post1 = self.driver.find_element_by_xpath("/html/body/div[4]/div[1]/div/div/a[2]")
                next_post1.click()

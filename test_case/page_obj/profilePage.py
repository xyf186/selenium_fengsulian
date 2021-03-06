import random,sys

sys.path.append("./public/common")
from public.common.base import *
from time import sleep
from public.common.log import Log

log = Log()

class ProfilePage(Page):
    '''
    个人资料
    '''
    #定位页面元素

    #当前登录用户
    current_user_loc = ("css selector",".loginIn.fl>span")
    #个人资料
    profile_loc = ("css selector",".nav_menu_bot>ul>li>a")
    #真实姓名
    reall_name_loc = ("css selector","#name")
    #性别（男）
    sex_male_loc = ("xpath",".//input[@value='男']")
    #性别（女）
    sex_female_loc = ("xpath",".//input[@value='女']")
    #电子邮箱
    email_loc = ("xpath",".//*[@id='email']")
    #位置（省、市、区）
    locator01 = ("css selector","#areaOut1")
    position_pro_loc = ("css selector","#sArea1Id>li")
    locator02 = ("css selector","#areaOut2")
    position_city_loc = ("css selector","#sArea2Id>li")
    locator03 = ("css selector", "#areaOut3")
    position_area_loc = ("css selector","#sArea3Id>li")
    #详细地址
    detail_address_loc = ("xpath",".//input[@name='address']")

    #头像
    edit_loc = ("css selector",".edit_pic.cropper")
    #选择文件
    choose_file_loc = ("xpath",".//input[@id='cropper_id']")
    path_file_loc = ("css selector","#cropper_id")
    up_file_loc = ("xpath",".//div[contains(text(),'确定上传')]")

    #确定
    submit_button_loc = ("xpath",".//input[@value='确定']")

    '''
    def __init__(self):
        初始化driver参数
        self.driver = browser('chrome')
    '''

    def open_profile(self):
        '''
        打开个人资料页面 
        '''
        self.move_to_element(self.current_user_loc)
        log.info("鼠标移动到个人资料：{}".format(self.current_user_loc))
        self.click(self.profile_loc)
        log.info("点击个人资料：{}".format(self.profile_loc))

    def real_name(self,name):
        '''
        输入真实姓名 
        '''
        self.send_keys(self.reall_name_loc,name,is_clear=True)
        log.info("输入真实姓名：{0}".format(self.reall_name_loc))

    def choose_sex01(self):
        '''
        选择性别
        '''
        self.click(self.sex_male_loc)
        log.info("选择性别：{}".format(self.sex_male_loc))

    def choose_sex02(self):
        '''
        选择性别（女）
        '''
        self.click(self.sex_female_loc)

    def email(self,email_address):
        '''
        输入邮箱 
        '''
        self.send_keys(self.email_loc,email_address,is_clear=True)
        log.info("定位邮箱输入框：{0},输入邮箱：{1}".format(self.email_loc,email_address))

    def choose_locator(self):
        '''
        选择位置 
        '''
        #先找到'位置'元素，然后点击
        self.click(self.locator01)
        sleep(2)
        elements = self.find_elements(self.position_pro_loc)
        #elements[3].click()
        
        i = random.randint(1,len(elements))
        elements[i].click()
        log.info("选择省：{}".format(elements[i].text))
        
        #选择市
        self.click(self.locator02)
        sleep(2)
        elements = self.find_elements(self.position_city_loc)
        #elements[3].click()
        
        i = random.randint(1,len(elements))
        elements[i].click()
        

        #选择县
        self.click(self.locator03)
        sleep(2)
        elements = self.find_elements(self.position_area_loc)
        #elements[1].click()
        
        i = random.randint(1,len(elements))
        elements[i].click()
        

    def detail_address(self,address_text):
        '''
        详细地址 
        '''
        self.send_keys(self.detail_address_loc,address_text,is_clear=True)
        log.info("定位地址输入框{0},输入详细地址{1}".format(self.detail_address_loc,address_text))
        sleep(2)

    def upload_photo(self,photo_path):
        '''
        上传头像 
        '''
        #点击编辑按钮
        self.click(self.edit_loc)
        log.info("定位并点击编辑按钮{}".format(self.edit_loc))
        sleep(2)
        #点击选择文件按钮
        #self.click(self.choose_file_loc)
        #sleep(3)
        
        self.send_keys(self.choose_file_loc,photo_path)
        log.info("定位选择文件按钮{}".format(self.choose_file_loc))
        self.click(self.up_file_loc)
        log.info("定位并点击确定上传按钮{}".format(self.up_file_loc))

    def submit(self):
        self.click(self.submit_button_loc)
        log.info("定位并点击个人资料页的确定按钮{}".format(self.submit_button_loc))

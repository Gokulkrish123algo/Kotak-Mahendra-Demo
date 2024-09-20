# pylint:disable=missing-function-docstring
# pylint: disable=missing-module-docstring
# pylint: disable=unused-wildcard-import
# pylint: disable=unused-import
import time
import re
import random
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import common
import imagecompareutil
import requestutil
from appium.webdriver.common.touch_action import TouchAction


def attach_page(context,pagename):
    if "browser" in str(context.mobileAutomationType).lower():
        try:
            pagename = int(pagename.replace('Page', ''))-1
            all_window_handles= context.driver.window_handles
            if pagename is not None:
                context.driver.switch_to.window(all_window_handles[pagename])
                return
            for handle in all_window_handles:
                context.driver.switch_to_window(handle)
                page_title = context.driver.title
                if pagename in page_title:
                    break
        except:
            pass

        
def buttonwhileusingtheappplicationclickifvisible(context):
    try:
        attach_page(context,'Current Screen')
    except:
        pass
    xpath = str(common.get_yml_object_repository_value(context.yamldataobject,"Current Screen","WhileUsingTheAppplicationButtonXPATH",context))
    common.butn_lnk_click_if_visible(context,"XPATH",xpath)
          
def buttonacceptthepopupclickifvisible(context):
    try:
        attach_page(context,'Current Screen')
    except:
        pass
    xpath = str(common.get_yml_object_repository_value(context.yamldataobject,"Current Screen","acceptthepopupButtonXPATH",context))
    common.butn_lnk_click_if_visible(context,"XPATH",xpath)
          
def buttonpdpcarticonselected(context):
    try:
        attach_page(context,'Current Screen')
    except:
        pass
    xpath = str(common.get_yml_object_repository_value(context.yamldataobject,"Current Screen","PDPCartIconButtonXPATH",context))
    common.button_selected(context,"XPATH",xpath)
    
def buttonclearallthewishlistproductsremoveallitemsbytap(context):
    i = 0    
    xpath = str(common.get_yml_object_repository_value(context.yamldataobject,"Current Screen","ClearalltheWishlistProductsButtonXPATH",context))
    while i < int(context.WhileLoopCount):
        try:
            if "**" in xpath:
                path = xpath.split('**')
                element1 = common.findElement(context,"XPATH",path[0])
                touch_actions = TouchAction(context.driver)
                touch_actions.tap(element1).perform()
                time.sleep(2)
                element2 = common.findElement(context,"XPATH",path[1])
                touch_actions = TouchAction(context.driver)
                touch_actions.tap(element2).perform()
                time.sleep(2)
            else:
                element = common.findElement(context,"XPATH",xpath)
                time.sleep(2)
                touch_actions = TouchAction(context.driver)
                touch_actions.tap(element).perform()
        except Exception:
            i += 1
        time.sleep(context.TimeIntervalInMilliSeconds)
        if i >= int(context.WhileLoopCount):
            break
    
def labelemptybagvfyverifytext(context):
    try:
        attach_page(context,'Current Screen')
    except:
        pass
    xpath = str(common.get_yml_object_repository_value(context.yamldataobject,"Current Screen","EmptyBagVfyLabelXPATH",context))
    return common.label_verify_text(context,"XPATH",xpath)
    
def buttonhomepagelogoselected(context):
    try:
        attach_page(context,'Current Screen')
    except:
        pass
    xpath = str(common.get_yml_object_repository_value(context.yamldataobject,"Current Screen","HomepageLogoButtonXPATH",context))
    common.button_selected(context,"XPATH",xpath)
    
def buttoncatagoriesselected(context):
    try:
        attach_page(context,'Current Screen')
    except:
        pass
    xpath = str(common.get_yml_object_repository_value(context.yamldataobject,"Current Screen","CatagoriesButtonXPATH",context))
    common.button_selected(context,"XPATH",xpath)
    
def buttonmakeupcverifytext(context):
    try:
        attach_page(context,'Current Screen')
    except:
        pass
    xpath = str(common.get_yml_object_repository_value(context.yamldataobject,"Current Screen","MakeupCButtonXPATH",context))
    return common.label_verify_text(context,"XPATH",xpath)
    
def buttonmakeupcselected(context):
    try:
        attach_page(context,'Current Screen')
    except:
        pass
    xpath = str(common.get_yml_object_repository_value(context.yamldataobject,"Current Screen","MakeupCButtonXPATH",context))
    common.button_selected(context,"XPATH",xpath)
    
def buttonfacemcverifytext(context):
    try:
        attach_page(context,'Current Screen')
    except:
        pass
    xpath = str(common.get_yml_object_repository_value(context.yamldataobject,"Current Screen","FaceMCButtonXPATH",context))
    return common.label_verify_text(context,"XPATH",xpath)
    
def buttonfacemcselected(context):
    try:
        attach_page(context,'Current Screen')
    except:
        pass
    xpath = str(common.get_yml_object_repository_value(context.yamldataobject,"Current Screen","FaceMCButtonXPATH",context))
    common.button_selected(context,"XPATH",xpath)
    
def linkfaceprimersmctap(context):
    try:
        attach_page(context,'Current Screen')
    except:
        pass
    xpath = str(common.get_yml_object_repository_value(context.yamldataobject,"Current Screen","FacePrimersMCLinkXPATH",context))
    common.tap_element(context,"XPATH", xpath)
          
def buttonplpaddtocartselected(context):
    try:
        attach_page(context,'Current Screen')
    except:
        pass
    xpath = str(common.get_yml_object_repository_value(context.yamldataobject,"Current Screen","PLPAddToCartButtonXPATH",context))
    common.button_selected(context,"XPATH",xpath)
    
def buttonavailableproductselected(context):
    try:
        attach_page(context,'Current Screen')
    except:
        pass
    xpath = str(common.get_yml_object_repository_value(context.yamldataobject,"Current Screen","AvailableProductButtonXPATH",context))
    common.button_selected(context,"XPATH",xpath)
    
def labelplaceordertextvfyverifytext(context):
    try:
        attach_page(context,'Current Screen')
    except:
        pass
    xpath = str(common.get_yml_object_repository_value(context.yamldataobject,"Current Screen","PlaceorderTextVfyLabelXPATH",context))
    return common.label_verify_text(context,"XPATH",xpath)
    
def buttondeleteproductselected(context):
    try:
        attach_page(context,'Current Screen')
    except:
        pass
    xpath = str(common.get_yml_object_repository_value(context.yamldataobject,"Current Screen","DeleteProductButtonXPATH",context))
    common.button_selected(context,"XPATH",xpath)
    
def buttonremoveproductselected(context):
    try:
        attach_page(context,'Current Screen')
    except:
        pass
    xpath = str(common.get_yml_object_repository_value(context.yamldataobject,"Current Screen","RemoveProductButtonXPATH",context))
    common.button_selected(context,"XPATH",xpath)
    
def pagedefaultpagedisplayed(context,var_page):
    try:
        attach_page(context,'Current Screen')
    except:
        pass
    return common.page_displayed(context, var_page, "xpath")
          
def labelmessagedisplayed(context,var_message):
    try:
        attach_page(context,'Current Screen')
    except:
        pass
    return common.label_displayed(context, var_message, "xpath")    
          
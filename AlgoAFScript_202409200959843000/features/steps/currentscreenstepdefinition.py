# pylint:disable=missing-function-docstring
# pylint: disable=missing-module-docstring
# pylint: disable=unused-wildcard-import
# pylint: disable=undefined-variable
# pylint: disable=function-redefined
import os
import sys
from behave import *
import currentscreenworkflow
import assertion

currentDir = os.getcwd()
previousDir = os.path.dirname(currentDir) + '/' + 'shared' + '/' + 'steps'
sys.path.append(previousDir)


def parse_string(text):
	return text.strip()


register_type(Name=parse_string)
use_step_matcher("cfparse")

        
@when("I click if visible While Using The Appplication in search")
def step(context):
     currentscreenworkflow.buttonwhileusingtheappplicationclickifvisible(context)
    
@when("I click if visible accept the popup in search")
def step(context):
     currentscreenworkflow.buttonacceptthepopupclickifvisible(context)
    
@when("I selected PDP Cart Icon in pdp")
def step(context):
     currentscreenworkflow.buttonpdpcarticonselected(context)
    
@when("I remove all items by tap Clear all the Wishlist Products in cart")
def step(context):
     currentscreenworkflow.buttonclearallthewishlistproductsremoveallitemsbytap(context)
    
@then("verify text Empty Bag Vfy in cart")
def step(context):
    assertion.assert_true(context,currentscreenworkflow.labelemptybagvfyverifytext(context))
    
@when("I selected Homepage Logo in search")
def step(context):
     currentscreenworkflow.buttonhomepagelogoselected(context)
    
@when("I selected Catagories in catagories home")
def step(context):
     currentscreenworkflow.buttoncatagoriesselected(context)
    
@then("verify text Makeup C in catagories home")
def step(context):
    assertion.assert_true(context,currentscreenworkflow.buttonmakeupcverifytext(context))
    
@when("I selected Makeup C in catagories home")
def step(context):
     currentscreenworkflow.buttonmakeupcselected(context)
    
@then("verify text Face M C in catagories home")
def step(context):
    assertion.assert_true(context,currentscreenworkflow.buttonfacemcverifytext(context))
    
@when("I selected Face M C in catagories home")
def step(context):
     currentscreenworkflow.buttonfacemcselected(context)
    
@when("I tap Face Primers M C in catagories home")
def step(context):
     currentscreenworkflow.linkfaceprimersmctap(context)
    
@when("I selected PLP Add To Cart in plp")
def step(context):
     currentscreenworkflow.buttonplpaddtocartselected(context)
    
@when("I selected Available Product in plp")
def step(context):
     currentscreenworkflow.buttonavailableproductselected(context)
    
@then("verify text Place order Text Vfy in cart")
def step(context):
    assertion.assert_true(context,currentscreenworkflow.labelplaceordertextvfyverifytext(context))
    
@when("I selected Delete Product in cart")
def step(context):
     currentscreenworkflow.buttondeleteproductselected(context)
    
@when("I selected Remove Product in cart")
def step(context):
     currentscreenworkflow.buttonremoveproductselected(context)
    
@then("'{var_page:Name?}' is displayed with '{var_content:Name?}'")
def step(context,var_page,var_content):
    assertion.assert_true(context,currentscreenworkflow.pagedefaultpagedisplayed(context,var_page))
    assertion.assert_true(context, currentscreenworkflow.labelmessagedisplayed(context,var_content))
    if str(context.softAssertion).lower() == 'true':
          assertion.assert_all(context)
    else:
          pass
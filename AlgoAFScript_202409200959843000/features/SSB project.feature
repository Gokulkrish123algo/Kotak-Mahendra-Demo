Feature: SSB project1
#Regression Type
#Correct Values = true
#Incorrect Values = false
#Illegal Values = false
#Invalid Values = false
#Boundary Values = false
#Edge Cases Values = false

@add_to_cart
@uid1770400075
@set21
@test001
Scenario Outline: verify user able to add the product to cart
Given I have access to application
When I click if visible While Using The Appplication in search
And I click if visible accept the popup in search
And I selected PDP Cart Icon in pdp
And I remove all items by tap Clear all the Wishlist Products in cart
Then verify text Empty Bag Vfy in cart
When I selected Homepage Logo in search
And I selected Catagories in catagories home
Then verify text Makeup C in catagories home
When I selected Makeup C in catagories home
Then verify text Face M C in catagories home
When I selected Face M C in catagories home
And I tap Face Primers M C in catagories home
And I selected PLP Add To Cart in plp
And I selected Available Product in plp
And I selected PDP Cart Icon in pdp
Then verify text Place order Text Vfy in cart
When I selected Delete Product in cart
And I selected Remove Product in cart
Then verify text Empty Bag Vfy in cart
And '<page>' is displayed with '<content>'

Examples:
|SlNo.|page|content|
|1|Current Screen|NA|

#Total No. of Test Cases : 1


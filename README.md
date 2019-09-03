
# The Beauty Corner 
In this project, I have chosen to make an E-commerce web-app. This app is make-up related, it provides a variety of make-up / skincare products which users can purchase and pay for by registering, if they are new to the website or log in if they are already members.
After picking their favourite product(s), users get transferred to the checkout page where they check their purchase and then enter their personal information to pay for the products.

# UX
This website is for make-up lovers, who like to buy makeup from the comfort of their houses for good prices. 
The product information consist of: prices, name of the product and a brief description about it along with a bar that allows the users to choose the number of items to buy.

Below are a couple of User experiences upon which the app was built:

1. As a user, I would like to have an account on the website for future use.
2. As a user, I would like to check my cart before paying and be able to make changes to it.
3. As a user, I would like the website to be easy to navigate. 

# Features :

# existing features
When a user is not a member:
1. the nav-bar only shows  SignIn, Register and Cart
2. when the user continues to the checkout, they will be asked to log in.

When a user is a logged in:
1. the nav-bar shows SignOut, My Account and Cart
2. My Account displays the user's information along with some extra information with may be useful to the user.

The Register form:
It asks the user to complete a form which consists of: their email, username that they wish to have, password and an extra field to confirm their password.

The LogIn form:
It asks the user to enter the username that they chose and their password.

Cart:
It displays the products picked and the total that the user has to pay, it has a checkout button which then takes the user to the payment page.

The products:
I have picked 6 products, 3 on each row. Each product has an image, a brief description, its price and a field on which they can choose the quantity and an "Add to cart" button.

My Account:
When the user is logged in, they can access their profile. On this page, they can see their information and some extra information which they might need.

# features left to implement 
I wanted to allow users to reset their passwords incase they have forgotten it, but there were some technical errors whenever i implement that feature.

# Technologies used
I have used various technologies, such as: HTML5, CSS3, Bootstrap- for writing and designing the website.
Javascript and Jquery were used to add functionality to the website.
I also used Python along with Django as a web framework for a rapid, secure website.
I added POSTGRESQL as a relational database in order to be able to add custom functions developed using the programming languages.

# Testing 
My webapp was tested for its responsivity by using the inspect function on the web browsers.
It was tested for its functionality by using the "python3 manage.py test" command, the tests passed.
The features I have on my website were made based on the UX scenarios for a better user experience.

To buy an item:
1. Register
2. Choose the product
3. Add to cart
4. Go to cart
5. Proceed to checkout 
6. Enter your details and submit payment

Bugs: In the checkout section, the number of items appears outside the box. (for unknown reasons)
After the user logs out after registering, it is unable to login even though new users are stored perfectly in the admin page. 
Moreover, the amend button in the checkout  shows an error when pressed due to technical problems. 

All the contents are visible on all screensizes and devices.

# Deployment
I have successfully pushed my files to my GitHub repository, went on heroku and connected my GitHub to the heroku app.
After that, I deployed it and ran my app. 
Development: is using Git commands to upload the file used in the making of the website to GitHub in order to be 
downloaded or viewed by the assesor and checked. To run my code locally, and ensure that it perfectly works, 
the user should download the source files used along with the HTML code and run it on their device.
 
# Credits

# Content :
The return policy on the user's profile - https://www.maccosmetics.com/customer-service-faq 

# Images: 
Jeffree Star makeup set - https://m.buro247.sg/images/beauty/beauty-bits-6thapril-buro247-CA.jpg
Wake Up & Go Mascara - https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ7mSPoRY4_MGy4bNtayXk8r1SUcki0uJClX3f5_NaeQf8IfJbN
The Mermaid Set - https://cf.shopee.co.th/file/448f917351a17710b7651876a754436a
Full make-up set - https://i.pinimg.com/originals/09/6d/a0/096da002dbac9af8d396d5ed56778f2e.jpg
NXN Skin Care - https://images-na.ssl-images-amazon.com/images/I/61FZhaQZsgL._SX450_.jpg
SIGMA Eyeshadow Palette - https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTeDstoUxtDjAMeveC5wz00R1kr9k0AWSKMKGTDXNKqS6JcAtRR_w
Pictures on the main page - https://i.pinimg.com/originals/fd/ec/4e/fdec4e4d43d1948af37e9c5a8a5e6f45.jpg
and https://cdn.fashionmagazine.com/wp-content/uploads/2017/03/Screen-Shot-2017-03-03-at-12.26.16-PM-480x480-c-top.png
# Acknowledgments 
This app was inspired by Beauty Bay Makeup website - https://www.beautybay.com/l/makeup/

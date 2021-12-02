# Import Webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Chrome Driver
driver = webdriver.Chrome(
    executable_path="E:/Programming Hero/Projects/rokomari-selenium-test/rokomari-python-selenium/chromedriver.exe"
)

# Test Result
test_result = {}

# Common Function
def sign_in():
    sign_in_link = driver.find_element(
        By.CSS_SELECTOR,
        "#js--main-header > div > div > div.col-3 > div > div.dropdown.user-menu > a",
    )

    sign_in_link.click()
    email_field = driver.find_element(By.ID, "j_username")
    password_field = driver.find_element(By.ID, "j_password")
    sign_in_btn = driver.find_element(By.CSS_SELECTOR, "#loginForm > button")

    email_field.send_keys("01688329403")
    password_field.send_keys("rifat123")
    sign_in_btn.send_keys(Keys.ENTER)

    if driver.current_url == "https://www.rokomari.com/book":
        test_result["Sign In Test"] = "Success"

    else:
        test_result["Sign In Test"] = "Failed"


# Home Page Test
driver.get("https://www.rokomari.com/book")
if driver.current_url == "https://www.rokomari.com/book":
    test_result["Home Page Test"] = "Success"

else:
    test_result["Home Page Test"] = "Failed"

# Sign In Test
sign_in()

# Profile Test
profile_dropdown = driver.find_element(By.CSS_SELECTOR, "#dropdownMenu2 > span")

# 1. My Account
profile_dropdown.click()
my_account = driver.find_element(
    By.CSS_SELECTOR,
    "#js--main-header > div > div > div.col-3 > div > div.dropdown.user-menu.show > div > a:nth-child(1)",
)
my_account.click()

# driver.find_element(By.ID, "js--edit-personal").click()

if driver.current_url == "https://www.rokomari.com/my-section/profile":
    test_result["My Account Test"] = "Success"

else:
    test_result["My Account Test"] = "Failed"


# 2. My Orders
driver.find_element(By.CSS_SELECTOR, "#dropdownMenu2 > span").click()
my_orders = driver.find_element(
    By.CSS_SELECTOR,
    "body > header > div > div > div > div > div.col-3 > div > div.dropdown.user-menu.show > div > a:nth-child(2)",
)
my_orders.click()

if driver.current_url == "https://www.rokomari.com/my-section/orders":
    test_result["My Orders Test"] = "Success"

else:
    test_result["My Orders Test"] = "Failed"

# 3. My list
# driver.find_element(By.CSS_SELECTOR, "#dropdownMenu2 > span").click()

# my_list = driver.find_element(
#     By.CSS_SELECTOR,
#     "body > header > div > div > div > div > div.col-3 > div > div.dropdown.user-menu.show > div > a:nth-child(3)",
# )
# my_list.click()

# create_new_list = driver.find_element(
#     By.CSS_SELECTOR,
#     "#my-account > div > div > div.col-9 > main > section > div.my-lists__heading.clearfix > a > button",
# )
# create_new_list.click()

# list_title = driver.find_element(By.ID, "list_title")
# list_title.send_keys("iphone")

# list_category = driver.find_element(
#     By.CSS_SELECTOR,
#     "#my-account > div > div > div.col-9 > main > section > div.my-list-create__content > form > div:nth-child(2) > select",
# )
# list_category.click()
# list_category.send_keys(Keys.ARROW_DOWN)
# list_category.send_keys(Keys.ENTER)

# list_type = driver.find_element(
#     By.CSS_SELECTOR,
#     "#my-account > div > div > div.col-9 > main > section > div.my-list-create__content > form > div:nth-child(3) > div:nth-child(3) > label",
# )
# list_type.click()

# list_description = driver.find_element(By.ID, "#products")

# driver.execute_script("arguments[1].click();", list_description)
# list_description.send_keys("a")
# list_description.send_keys(Keys.ARROW_DOWN)
# list_description.send_keys(Keys.ENTER)

# 4. My wishlist
driver.find_element(By.CSS_SELECTOR, "#dropdownMenu2 > span").click()
wishlist = driver.find_element(
    By.CSS_SELECTOR,
    "body > header > div > div > div > div > div.col-3 > div > div.dropdown.user-menu.show > div > a:nth-child(4)",
)
wishlist.click()

if driver.current_url == "https://www.rokomari.com/my-section/wish-list":
    test_result["My Wishlist Test"] = "Success"

else:
    test_result["My Wishlist Test"] = "Failed"

# 5. My rating review
driver.find_element(By.CSS_SELECTOR, "#dropdownMenu2 > span").click()
rating = driver.find_element(
    By.CSS_SELECTOR,
    "body > header > div > div > div > div > div.col-3 > div > div.dropdown.user-menu.show > div > a:nth-child(5)",
)
rating.click()

if (
    driver.current_url
    == "https://www.rokomari.com/my-section/reviews/not-reviewed?ref=my_review"
):
    test_result["My Rating Review Test"] = "Success"

else:
    test_result["My Rating Review Test"] = "Failed"

# 6. My points
driver.find_element(By.CSS_SELECTOR, "#dropdownMenu2 > span").click()
points = driver.find_element(
    By.CSS_SELECTOR,
    "body > header > div > div > div > div > div.col-3 > div > div.dropdown.user-menu.show > div > a:nth-child(6)",
)
points.click()

if driver.current_url == "https://www.rokomari.com/my-section/point":
    test_result["My Points Test"] = "Success"

else:
    test_result["My Points Test"] = "Failed"

# 7. Sign out
driver.find_element(By.CSS_SELECTOR, "#dropdownMenu2 > span").click()
signout_btn = driver.find_element(
    By.CSS_SELECTOR,
    "body > header > div > div > div > div > div.col-3 > div > div.dropdown.user-menu.show > div > a:nth-child(8)",
)
signout_btn.click()

if driver.current_url == "https://www.rokomari.com/book":
    test_result["My Singout Test"] = "Success"

else:
    test_result["My Singout Test"] = "Failed"

# Search Test
search_field = driver.find_element(
    By.CSS_SELECTOR,
    "#js--search",
)
search_field.send_keys("book")
search_field.send_keys(Keys.ENTER)

# Notification Test
sign_in()
# notification = driver.find_element(
#     By.CSS_SELECTOR,
#     "body > header > div > div > div > div > div.col-3 > div > div.notification-wrapper > nav > ul > a",
# )
# notification.click()
# test_result["Notification Test"] = "Success"

# Cart Test
cart = driver.find_element(
    By.CSS_SELECTOR,
    "#cart-icon",
)
cart.click()

if driver.current_url == "https://www.rokomari.com/cart":
    test_result["My Cart Test"] = "Success"

else:
    test_result["My Cart Test"] = "Failed"

# Top Bar Test
# 1. Book
book = driver.find_element(
    By.CSS_SELECTOR,
    "body > header > div > nav > div > div > ul > li:nth-child(1) > a",
)
book.click()

if driver.current_url == "https://www.rokomari.com/book?ref=nm":
    test_result["My Book Test"] = "Success"

else:
    test_result["My Book Test"] = "Failed"

# 2. Electronics
electronice = driver.find_element(
    By.CSS_SELECTOR,
    "body > header > div > nav > div > div.container-fluid.custom-container > ul > li:nth-child(2) > a",
)
electronice.click()

if driver.current_url == "https://www.rokomari.com/electronics?ref=nm":
    test_result["My Electronics Test"] = "Success"

else:
    test_result["My Electronics Test"] = "Failed"

# 3. Stationary and others
stationary = driver.find_element(
    By.CSS_SELECTOR,
    "body > header > div > nav > div > div.container-fluid.custom-container > ul > li.main-menu-active",
)
stationary.click()

if driver.current_url == "https://www.rokomari.com/stationary?ref=nm":
    test_result["My Stationary Test"] = "Success"

else:
    test_result["My Stationary Test"] = "Failed"

# 4. Gift Finder
gift_finder = driver.find_element(
    By.CSS_SELECTOR,
    "body > header > div > nav > div > div.container-fluid.custom-container > ul > li:nth-child(4) > a",
)
gift_finder.click()

if driver.current_url == "https://www.rokomari.com/giftfinder?ref=nm":
    test_result["Gift Finder Test"] = "Success"

else:
    test_result["Gift Finder Test"] = "Failed"

# 5. Institutional order
institutional = driver.find_element(
    By.CSS_SELECTOR,
    "body > header > div > nav > div > div.container-fluid.custom-container > ul > li:nth-child(5) > a",
)
institutional.click()

if driver.current_url == "https://www.rokomari.com/corporate?ref=nm":
    test_result["Gift Institutional Order Test"] = "Success"

else:
    test_result["Gift Institutional Order Test"] = "Failed"

# 6. Offers
offers = driver.find_element(
    By.CSS_SELECTOR,
    "body > header > div > nav > div > div.container-fluid.custom-container > ul > li:nth-child(6) > a",
)
offers.click()

if driver.current_url == "https://www.rokomari.com/offer?ref=nm":
    test_result["Offers Test"] = "Success"

else:
    test_result["Offers Test"] = "Failed"

# 7. Blog
blog = driver.find_element(
    By.CSS_SELECTOR,
    "body > header > div > nav > div > div > ul > li:nth-child(7) > a",
)
blog.click()

if driver.current_url == "https://blog.rokomari.com/?ref=nm":
    test_result["Blog Test"] = "Success"

else:
    test_result["Blog Test"] = "Failed"


# Print Test Result
print(test_result)

# Quit Driver
# driver.quit()

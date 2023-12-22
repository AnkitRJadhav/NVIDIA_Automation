*** Settings ***
Library    ../Library/NVIDIA.py
Library    Screenshot
Library    SeleniumLibrary
Variables    ../locators/NVIDIA.yaml
Variables    ../Environment/app_config.yaml

*** Keywords ***
Open_And_Validate_Product_Tab
    ${driver}    open_browser_nvidia    ${Config.Browser}
    Capture Page Screenshot
    launch_site   ${driver}    ${Config.URL}
    Capture Page Screenshot
    click_product_tab    ${driver}    ${Locators.Product_Tab}
    Capture Page Screenshot
    select_laptop_from_product_tab     ${driver}    ${Locators.Laptop_Button}


Open_And_Validate_Solution_Tab
    ${driver}    open_browser_nvidia    ${Config.Browser}
    Capture Page Screenshot
    launch_site   ${driver}    ${Config.URL}
    Capture Page Screenshot
    click_solution_tab    ${driver}    ${Locators.Solution_Tab}
    Capture Page Screenshot
    select_cloud_from_solution_tab     ${driver}    ${Locators.Cloud_button}
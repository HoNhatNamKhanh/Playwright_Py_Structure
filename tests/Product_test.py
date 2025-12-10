import pytest
from pages.product_page import ProductPage

def test_search_product(page):
    # Khởi tạo trang
    product_page = ProductPage(page)

    # Base URL (có thể nằm trong config, env, hoặc fixture)
    base_url = "https://juno.vn/collections/san-pham-moi-nhat?itm_source=homepage&itm_medium=menu&itm_campaign=normal&itm_content=sanpham"

    # Điều hướng đến trang sản phẩm
    product_page.goto(base_url)

    # Search
    product_page.search_product("Laptop")

    # Lấy số sản phẩm trả về
    count = product_page.get_product_count()

    # Assertion
    assert count > 0, "Expected at least one product but got zero."

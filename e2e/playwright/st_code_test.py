# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from playwright.sync_api import Page, expect

from conftest import ImageCompareFunction


def test_code_display(app: Page):
    """Test that st.code displays a code block."""
    code_element = app.locator(".element-container pre").first
    expect(code_element).to_contain_text("This code is awesome!")


def test_syntax_highlighting(themed_app: Page, assert_snapshot: ImageCompareFunction):
    """Test that the copy-to-clipboard action appears on hover."""
    first_code_element = themed_app.locator(".element-container:first-child pre").first
    first_code_element.hover()
    assert_snapshot(first_code_element, name="syntax_highlighting-hover")


def test_code_blocks_render_correctly(
    themed_app: Page, assert_snapshot: ImageCompareFunction
):
    """Test that the code blocks render as expected via screenshot matching."""
    code_blocks = themed_app.get_by_test_id("stCodeBlock")

    assert_snapshot(code_blocks.nth(0), name="st_code-auto_lang")
    assert_snapshot(code_blocks.nth(1), name="st_code-empty")
    assert_snapshot(code_blocks.nth(2), name="st_code-python_lang")
    assert_snapshot(code_blocks.nth(3), name="st_code-line_numbers")
    assert_snapshot(code_blocks.nth(4), name="st_code-no_lang")


def test_code_in_markdown(app: Page, assert_snapshot: ImageCompareFunction):
    """Test that the syntax highlighting is applied correctly to the code block."""
    expander_with_code = app.get_by_test_id("stExpander")

    assert_snapshot(expander_with_code.nth(0), name="expander_with_code")
    assert_snapshot(expander_with_code.nth(1), name="expander_with_markdown_code")

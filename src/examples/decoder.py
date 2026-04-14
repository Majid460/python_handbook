from typing import List, Tuple, Optional

import requests
from bs4 import BeautifulSoup


def display_message(grid: List[List[str]]):
    # Print the final decoded message
    if not grid:
        print("Nothing to display")
        return
    for row in grid:
        print(" ".join(row))
    # Debug — print total columns
    print(f"\nGrid size: {len(grid)} rows x {len(grid[0])} cols")


def data_processing(points: List[Tuple[str, int, int]]) -> List[List[str]]:
    # Find the boundaries of grid
    max_x = max(x for _, x, _ in points)
    max_y = max(y for _, _, y in points)

    # The axis with larger range is horizontal (cols)
    # The axis with smaller range is vertical (rows)
    if max_x >= max_y:
        # x = col (horizontal), y = row (vertical)
        rows = max_y + 1
        cols = max_x + 1
        grid = [[" " for _ in range(cols)] for _ in range(rows)]
        for char, x, y in points:
            if y < rows and x < cols:  # boundary guard
                grid[y][x] = char
    else:
        # x = row (vertical), y = col (horizontal)
        rows = max_x + 1
        cols = max_y + 1
        grid = [[" " for _ in range(cols)] for _ in range(rows)]
        for char, x, y in points:
            if x < rows and y < cols:  # boundary guard
                grid[x][y] = char

    return grid


def data_extraction(all_rows) -> Optional[List[Tuple[str, int, int]]]:
    points: List[Tuple[str, int, int]] = []

    for row in all_rows[1:]:
        cols = row.find_all("td")
        if len(cols) != 3:
            continue
        try:
            x = int(cols[0].text.strip())
            char = cols[1].text.strip()
            y = int(cols[2].text.strip())
            points.append((char, x, y))
        except ValueError:
            continue  # skip any malformed row

    return points if points else None


def decode_secret_message(url: str):
    # Fetch the published google doc
    response = requests.get(url)
    response.raise_for_status()

    # Parse raw html into navigatable DOM tree
    soup = BeautifulSoup(response.text, "html.parser")

    # Extract all table rows
    all_rows = soup.find_all("tr")

    # Extract, process and display
    points = data_extraction(all_rows)

    if not points:
        print("Invalid data")
        return

    grid = data_processing(points)
    display_message(grid)


if __name__ == "__main__":
    decode_secret_message(
        "https://docs.google.com/document/d/e/2PACX-1vSvM5gDlNvt7npYHhp_XfsJvuntUhq184By5xO_pA4b_gCWeXb6dM6ZxwN8rE6S4ghUsCj2VKR21oEP/pub"
    )

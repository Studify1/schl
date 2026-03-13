from pyscript import display


# Display in a specific element by ID.
display("Hello mada this is my first PyScript!", target="output-div")

# The '#' prefix is optional (and ignored if present).
display("Hello", target="#output-div")

from pyscript import web


# Get an existing select element.
select = web.page["my-select"]

# Add options.
select.options.add(value="1", html="Option 1")
select.options.add(value="2", html="Option 2", selected=True)

# Get the selected option.
selected = select.options.selected
print(f"Selected: {selected.value}")

# Iterate over options.
for option in select.options:
    print(f"{option.value}: {option.innerHTML}")

# Clear all options.
select.options.clear()

# Remove specific option by index.
select.options.remove(0)

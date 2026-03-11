from pyscript import document
print("Hello, World in console!")
output_div = document.getElementById("textarea")
output_div.innerText = "Hello, World! from pyscript"
output_div.style.color = "red"
output_div.style.fontSize = "24px"
output_div.style.fontWeight = "bold"
output_div.style.textAlign = "center"

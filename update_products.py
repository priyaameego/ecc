with open("e:/ecc/products.html", "r", encoding="utf-8") as f:
    content = f.read()

content = content.replace("grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8", "grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-5 gap-4 md:gap-6")

replacements = {
    "<i class=\"fas fa-bolt text-6xl text-gold-400/80 group-hover:scale-110 transition-transform duration-500\"></i>": "<img src=\"assets/prod_kordy_x.png\" alt=\"KORDY X\" class=\"h-40 w-auto object-contain drop-shadow-2xl group-hover:scale-110 transition-transform duration-500\">",
    "<i class=\"fas fa-leaf text-6xl text-gold-400/80 group-hover:scale-110 transition-transform duration-500\"></i>": "<img src=\"assets/prod_ashwagandha.png\" alt=\"Ashwagandha Plus\" class=\"h-40 w-auto object-contain drop-shadow-2xl group-hover:scale-110 transition-transform duration-500\">",
    "<i class=\"fas fa-mountain text-6xl text-gold-400/80 group-hover:scale-110 transition-transform duration-500\"></i>": "<img src=\"assets/prod_shilajit.png\" alt=\"Shilajit Gold\" class=\"h-40 w-auto object-contain drop-shadow-2xl group-hover:scale-110 transition-transform duration-500\">",
    "<i class=\"fas fa-fire text-6xl text-gold-400/80 group-hover:scale-110 transition-transform duration-500\"></i>": "<img src=\"assets/prod_gokshura.png\" alt=\"Gokshura Power\" class=\"h-40 w-auto object-contain drop-shadow-2xl group-hover:scale-110 transition-transform duration-500\">",
    "<i class=\"fas fa-seedling text-6xl text-gold-400/80 group-hover:scale-110 transition-transform duration-500\"></i>": "<img src=\"assets/prod_ginseng.png\" alt=\"Panax Ginseng\" class=\"h-40 w-auto object-contain drop-shadow-2xl group-hover:scale-110 transition-transform duration-500\">",
    "<i class=\"fas fa-spa text-6xl text-gold-400/80 group-hover:scale-110 transition-transform duration-500\"></i>": "<img src=\"assets/prod_chaste.png\" alt=\"Chaste Tree Blend\" class=\"h-40 w-auto object-contain drop-shadow-2xl group-hover:scale-110 transition-transform duration-500\">",
    "<i class=\"fas fa-box-open text-6xl text-gold-400/80 group-hover:scale-110 transition-transform duration-500\"></i>": "<img src=\"assets/prod_kordy_x.png\" alt=\"KORDY X\" class=\"h-40 w-auto object-contain drop-shadow-2xl group-hover:scale-110 transition-transform duration-500\">",
    "<i class=\"fas fa-bone text-6xl text-gold-400/80 group-hover:scale-110 transition-transform duration-500\"></i>": "<img src=\"assets/prod_joyflex.png\" alt=\"JOYFLEX PLUS\" class=\"h-40 w-auto object-contain drop-shadow-2xl group-hover:scale-110 transition-transform duration-500\">"
}

for old, new in replacements.items():
    content = content.replace(old, new)

content = content.replace("text-2xl mb-2 text-white", "text-xl mb-1 text-white")
content = content.replace("p-6", "p-4")

with open("e:/ecc/products.html", "w", encoding="utf-8") as f:
    f.write(content)

# store.py
def store(owner, *products, **details):
    filename = "store.txt"
    with open(filename, "a") as file:
        file.write(f"Owner: {owner}\n")
        file.write("Products:\n")
        for i, item in enumerate(products, 1):
            file.write(f"{i}. {item}\n")
        file.write("Details:\n")
        for k, v in details.items():
            file.write(f"{k} : {v}\n")
        file.write("\n" + "-"*30 + "\n")
    print(f"تم حفظ بيانات المتجر في {filename} ✅")


if __name__ == "__main__":
    # مثال استخدام
    store(
        "Abdo",
        "Laptop",
        "Phone",
        "Headset",
        city="Kuala Lumpur",
        open_time="8 - AM",
        worker=12
    )

    # قراءة الملف
    print("\n📝 محتوى الملف:")
    with open("store.txt", "r") as file:
        print(file.read())
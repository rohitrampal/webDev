import qrcode

code_q = qrcode.QRCode(box_size = 35, border = 4)
code_q.add_data("https://www.youtube.com/watch?v=szZrVN6UQM4")
code_q.make(fit=True)

qrcode_imp = code_q.make_image(fill_color="black",back_color="white")
qrcode_imp.save("imgqrcode.png")

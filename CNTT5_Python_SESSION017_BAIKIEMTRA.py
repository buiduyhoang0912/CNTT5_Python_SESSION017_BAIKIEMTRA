danhsach = [
    {
        "ma" : "CT007",
        "hoten" : "Nguyen Quang Hai ",
        "sotran" : 10,
        "banthang" : 5,
        "kientao" : 4,
        "diemhieusuat" : 33,
        "phanloai" : "Trụ cột đội bóng"
    }
]

def hienthi(danhsach) :
    print("=== DANH SÁCH ĐỘI BÓNG ===")
    print(f"{'Mã CT' :<10} | {'Họ và tên' :<25} | {'Số trận' :<10} | {'Số bàn thắng' :<15} | {'Số kiến tạo' :<15} | {'Điểm hiệu suất' :<15} | {'Phân loại phong độ' :<30} |")
    for i in danhsach : 
        print(f"{i['ma'] :<10} | {i['hoten'] :<25} | {i['sotran'] :<10} | {i['banthang'] :<15} | {i['kientao']:<15} | {i['diemhieusuat'] :<15} | {i['phanloai'] :<30} |")

def trong(a) :
    if a == "" :
        return True 
    return False 

def trung(a,danhsach) :
    for i in range(len(danhsach)) : 
        if a == danhsach[i]['ma'] :
            return i 
    return False 

def so(a) :
    if not a.isdigit() :
        return True 
    return False 

def phanloai(a) :
    if a < 15 :
        return("Cần thanh lý / Cho mượn")
    elif a < 30 :
        return("Dự bị chiến lược")
    elif a < 50 :
        return("Trụ cột đội bóng")
    else : 
        return("Ngôi sao đẳng cấp")

def trungten(a,danhsach) :
    for i in range(len(danhsach)) : 
        if a.lower() in danhsach[i]['hoten'].lower() :
            return i
    return False 

def tiepnhan(danhsach) :
    while True :
        ma = input("Nhập mã cầu thủ : ").strip().upper()
        if trong(ma) :
            print("Mã không được để trống ! Vui lòng nhập lại")
            continue
        if trung(ma,danhsach) != False or (len(danhsach) > 0 and danhsach[0]['ma'] == ma):
            print("Mã đã tồn tại ! Vui lòng nhập lại")
            continue
        break 

    while True : 
        ten = input("Nhập tên cầu thủ : ").strip().title()
        if trong(ten) :
            print("Tenn khôngg được để trống ! Vui lòng nhạp lại")
            continue 
        break 

    while True : 
        sotran = input("Nhập số trận bóng : ").strip()
        if trong(sotran) :
            print("Số trận không được để trống ! Vui lòng nhập lại")
            continue 
        if so(sotran) :
            print("Số trận bóng khôgn hợp lệ ! Vui lòng nhập lại")
            continue 
        if not (0 <= int(sotran) <= 50):
            print("Số trận phải nằm trong khoảng từ 0 đến 50 ! Vui lòng nhập lại")
            continue
        break 

    while True : 
        banthang = input("Nhập số bàn thắng : ").strip()
        if trong(banthang) :
            print("Số bàn thắng không được để trống ! Vui lòng nhập lại")
            continue 
        if so(banthang) :
            print("Số bàn thắng khôgn hợp lệ ! Vui lòng nhập lại")
            continue 
        break 

    while True : 
        kientao = input("Nhập số kiến tạo : ").strip()
        if trong(kientao) :
            print("Số kiến tạo không được để trống ! Vui lòng nhập lại")
            continue 
        if so(kientao) :
            print("Số kiến tạo khôgn hợp lệ ! Vui lòng nhập lại")
            continue 
        break 

    sotran = int(sotran)
    banthang = int(banthang)
    kientao = int(kientao)
    hieusuat = (sotran*1) + (banthang*3) + (kientao*2)
    phanloai1 = phanloai(hieusuat)

    new = {
        "ma" : ma,
        "hoten" : ten,
        "sotran" : sotran,
        "banthang" : banthang,
        "kientao" : kientao,
        "diemhieusuat" : hieusuat,
        "phanloai" : phanloai1
    }
    danhsach.append(new)
    
def capnhat(danhsach) : 
    while True :
        ma = input("Nhập mã cầu thủ : ").strip().upper()
        if trong(ma) :
            print("Mã không được để trống ! Vui lòng nhập lại")
            continue
        
        value = trung(ma,danhsach)
        if value != False or (len(danhsach) > 0 and danhsach[0]['ma'] == ma):
            if value == False:
                value = 0

            while True : 
                sotran = input("Nhập số trận bóng mới : ").strip()
                if trong(sotran) :
                    print("Số trận không được để trống ! Vui lòng nhập lại")
                    continue 
                if so(sotran) :
                    print("Số trận bóng khôgn hợp lệ ! Vui lòng nhập lại")
                    continue 
                if not (0 <= danhsach[value]['sotran'] + int(sotran) <= 50):
                    print("Tổng số trận vượt quá giới hạn 50 ! Vui lòng nhập lại")
                    continue
                danhsach[value]['sotran'] += int(sotran)
                break 

            while True : 
                banthang = input("Nhập số bàn thắng mới : ").strip()
                if trong(banthang) :
                    print("Số bàn thắng không được để trống ! Vui lòng nhập lại")
                    continue 
                if so(banthang) :
                    print("Số bàn thắng khôgn hợp lệ ! Vui lòng nhập lại")
                    continue 
                danhsach[value]['banthang'] += int(banthang)
                break 

            while True : 
                kientao = input("Nhập số kiến tạo mới : ").strip()
                if trong(kientao) :
                    print("Số kiến tạo không được để trống ! Vui lòng nhập lại")
                    continue 
                if so(kientao) :
                    print("Số kiến tạo khôgn hợp lệ ! Vui lòng nhập lại")
                    continue 
                danhsach[value]['kientao'] += int(kientao)
                break  
            
            danhsach[value]['diemhieusuat'] = (danhsach[value]['sotran']*1) + (danhsach[value]['banthang']*3) + (danhsach[value]['kientao']*2)
            danhsach[value]['phanloai'] = phanloai(danhsach[value]['diemhieusuat'])
            print("Cập nhật thông tin thành công!")
        else:
            print("Không tìm thấy mã cầu thủ!")   
        break 

def xoa(danhsach) :
    while True :
        ma = input("Nhập mã cầu thủ : ").strip().upper()
        if trong(ma) :
            print("Mã không được để trống ! Vui lòng nhập lại")
            continue
        
        value = trung(ma,danhsach)
        if value != False or (len(danhsach) > 0 and danhsach[0]['ma'] == ma):
            if value == False:
                value = 0
            while True : 
                ykien = input("Bạn có muốn chắc chắn xóa cầu thủ này khỏi danh sách không(Y/N) : ").strip().upper()
                match ykien : 
                    case "Y" :
                        danhsach.pop(value)
                        print("Đã xóa thành công")
                        return 
                    case "N" :
                        print("Xử lý thành công")
                        return
                    case _:
                        print("Lựa chọn không hợp lệ ! Vui lòng nhập lại")
        else:
            print("Không tìm thấy mã cầu thủ cần xóa!")
            return
            
def tim(danhsach) :
    while True : 
        ykien = input("Bạn muốn tìm kiếm cầu thủ theo gì (ma/ten) : ").strip()
        match ykien : 
            case "ma" :
                while True :
                    ma = input("Nhập mã cầu thủ : ").strip().upper()
                    if trong(ma) :
                        print("Mã không được để trống ! Vui lòng nhập lại")
                        continue
                    
                    value = trung(ma,danhsach)
                    if value != False or (len(danhsach) > 0 and danhsach[0]['ma'] == ma):
                        if value == False:
                            value = 0
                        print("=== KẾT QUẢ TÌM KIẾM ===")
                        print(f"{'Mã CT' :<10} | {'Họ và tên' :<25} | {'Số trận' :<10} | {'Số bàn thắng' :<15} | {'Số kiến tạo' :<15} | {'Điểm hiệu suất' :<15} | {'Phân loại phong độ' :<30} |")
                        i = danhsach[value]
                        print(f"{i['ma'] :<10} | {i['hoten'] :<25} | {i['sotran'] :<10} | {i['banthang'] :<15} | {i['kientao']:<15} | {i['diemhieusuat'] :<15} | {i['phanloai'] :<30} |")
                        return 
                    else:
                        print("Không tìm thấy cầu thủ")
                        return
            case "ten" :
                while True :
                    ten = input("Nhập họ tên cầu thủ : ").strip()
                    if trong(ten) :
                        print("Tên không được để trống ! Vui lòng nhập lại")
                        continue
                    
                    ketqua = []
                    for i in range(len(danhsach)):
                        if ten.lower() in danhsach[i]['hoten'].lower():
                            ketqua.append(danhsach[i])
                            
                    if len(ketqua) > 0:
                        print("=== KẾT QUẢ TÌM KIẾM ===")
                        print(f"{'Mã CT' :<10} | {'Họ và tên' :<25} | {'Số trận' :<10} | {'Số bàn thắng' :<15} | {'Số kiến tạo' :<15} | {'Điểm hiệu suất' :<15} | {'Phân loại phong độ' :<30} |")
                        for i in ketqua:
                            print(f"{i['ma'] :<10} | {i['hoten'] :<25} | {i['sotran'] :<10} | {i['banthang'] :<15} | {i['kientao']:<15} | {i['diemhieusuat'] :<15} | {i['phanloai'] :<30} |")
                        return
                    else:
                        print("Không tìm thấy cầu thủ")
                        return
            case _:
                print("Lựa chọn không hợp lệ ! Vui lòng nhập lại")

def thongke(danhsach) :
    a = 0
    b = 0 
    c = 0 
    d = 0
    for i in danhsach :
        if i["phanloai"] == "Cần thanh lý / Cho mượn" :
            a += 1
        elif i["phanloai"] == "Dự bị chiến lược" : 
            b += 1
        elif i["phanloai"] == "Trụ cột đội bóng" : 
            c += 1
        elif i["phanloai"] == "Ngôi sao đẳng cấp" : 
            d += 1
    print(
f"""
=== THỐNG KÊ BIỂU ĐỒ SỐ LƯỢNG NHÂN SỰ ===
Ngôi sao đẳng cấp : {d} cầu thủ
Trụ cột đội bóng  : {c} cầu thủ
Dự bị chiến lược  : {b} cầu thủ
Cần thanh lý      : {a} cầu thủ
"""
    )

def thoat() :
    print("Thoát chương trình. Tạm biệt và hẹn gặp lại!")
    return

check = 0
while check != "8" :
    print(
f"""
=== MENU ===
1. Hiển thị danh sách cầu thủ 
2. Tiếp nhận cầu thủ mới 
3. Cập nhật thông tin và chỉ số 
4. Xóa cầu thủ(Thanh lý hợp đồng)
5. Tìm kiếm cầu thủ
6. Thống kê phân loại phong độ 
8. Thoát chương trình
"""
    )
    check = input("Nhập lựa chọn của bạn : ").strip()
    match check :
        case "1" :
            hienthi(danhsach)
        case "2" : 
            tiepnhan(danhsach)
        case "3" :
            capnhat(danhsach) 
        case "4" :
            xoa(danhsach)
        case "5" :
            tim(danhsach)
        case "6" :
            thongke(danhsach)
        case "8" :
            thoat()
        case _:
            print("Lựa chọn không hợp lệ ! Vui lòng nhập lại")

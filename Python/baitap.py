import random
import numpy as np
import copy
def bai14():
    a=[]#khởi tạo mãng
    m=int(input("Nhập số dòng"))
    n=int(input("Nhập số cột"))
    #điền số dòng
    for i in range(m):
        row=[]
        for j in range(n):
            row.append(random.randint(0,99))
        a.append(row)
    #in ra mãng 2 chiều
    print("Mảng a: ")
    for row in a:
        print(row)
     # chuyển list sang numpy array
    arr = np.array(a)
    #b.Xuất các phần tử thuộc dòng k
    k = int(input("Nhập dòng bạn muốn xuất"))
    print(arr[k])

    #c.Xuất các phần tử thuộc cột k.
    h=int(input("Nhập cột bạn muốn tìm: "))
    print(arr[: , h]) 
    # d. Tìm dòng có tổng số lớn nhất
    maxsum = 0
    maxindex = 0
    for idx, row in enumerate(a):   # vừa lấy chỉ số, vừa lấy dòng
        s = sum(row)                # tính tổng nhanh hơn
        if s > maxsum:
            maxsum = s
            maxindex = idx          # lưu lại chỉ số dòng

    print(f"Tổng dòng lớn nhất là {maxsum}")
    print("Dòng có tổng lớn nhất:", arr[maxindex])

    #e.	Tìm cột có tích nhỏ nhất. 
    mintich=None
    minindex= 0 
    # số cột = số phần tử trong mỗi hàng
    for j in range(len(a[0])):
        tich = 1
        for i in range(len(a)):
            tich *= a[i][j]   # nhân các phần tử trong cột j
        if mintich is None or tich < mintich:
            mintich = tich
            minindex = j

    print(f"Tích nhỏ nhất của một cột là {mintich}")
    print("Cột có tích nhỏ nhất:", [a[i][minindex] for i in range(len(a))])

    #f.	Xuất ra các phần tử thuộc dòng chẵn và cột lẻ trong a. 
    for i in range(len(a)):
        if i%2==0:
            for j in range(len(a[0])):
                if(j%2!=0):
                    print (f"[{a[i][j]}]")
    #g.	Tính trung bình cộng các phần tử chẵn thuộc dòng lẻ của a.
    trungbinh=0
    for i in range(len(a)):
        if i%2!=0:
            trungbinh+=np.average(a[i]) 

    print (f"Trung bình cộng các dòng lẻ trong a: {trungbinh}")
    #h.	Tính trung bình cộng các phần tử thuộc biên. 
    tong =0
    dem =0
    for i in range(len(a)):
        for j in range(len(a[0])):
            if i == 0 or i == len(a)-1 or j == 0 or j == len(a[0])-1:
                tong+=a[i][j]
                dem+=1
    if dem>0:
        tb_bien=tong/dem
        print(f"Trung bình cộng các phần tử thuộc biên a: {tb_bien}")
    else:
        print("Không có phần tử thuộc biên.")
     #i.	Tính trung bình tích các phần tử không thuộc biên.  
    tong_i =0
    dem_i =0
    for i in range(len(a)):
        for j in range(len(a[0])):
            if i != 0 and i != len(a)-1 and j != 0 and j != len(a[0])-1:
                tong_i+=a[i][j]
                dem_i+=1
    if dem_i>0:
        tb_kobien=tong_i/dem_i
        print(f"Trung bình cộng các phần tử không thuộc biên a: {tb_kobien}")
    else:
        print("Không có phần tử không thuộc biên.")
bai14()
# a. Xây dựng cấu trúc SINHVIEN
class sinhvien:
    def __init__(sv, masv, tensv, namsinh, diemtb):
        sv.masv= masv #10 ký tự
        sv.tensv= tensv #20 ký tự
        sv.namsinh =namsinh #int
        sv.diemtb = diemtb #float
#b. Cho một mảng có n sinh viên
ds_dv =[sinhvien("10DH0023","Lan",2006,8.9),
        sinhvien("22DH2321","Phan An",2005,7.9),
        sinhvien("21CD3243","Lam Anh",2004,3),
        sinhvien("11DH3322","Lan",2006,8.9)
        ]
#c.	Viết hàm cho biết có bao sinh viên đủ điều kiện lên lớp, biết rằng sinh viên đủ điều kiện lên lớp khi điểm trung bình lớn hơn hoặc bằng 5. 
def ds_du_dk(ds):
    count=0
    for sv in ds:
        if sv.diemtb>=5:
            count+=1
    return(count)
print("Số sinh viên đủ điều kiện lên lớp:", ds_du_dk(ds_dv))
#d.	Xuất các sinh viên đủ 20 tuổi. 
def ds_du_20(ds):
    for sv in ds:
        if 2026 - sv.namsinh==20:
            print(f"{sv.masv} - {sv.tensv} - {sv.namsinh} - {sv.diemtb}")

ds_du_20(ds_dv)

#e.	Đếm số sinh viên học hệ đại học, biết rằng sinh viên hệ DH có mã sinh viên chứa 2 ký tự DH ở vị trí 2,3 trong chuỗi. VD: 02DH0001. 
def count_sv_dh(ds):
    count=0
    for sv in ds:
        if (sv.masv[2:4]=="DH"):
            count+=1
    return count
print("Số sinh viên hệ đại học:", count_sv_dh(ds_dv))

#f.	Cho biết trong mảng có bao nhiêu sinh viên có tên «Lan» 
def find_sv_lan(ds):
    count =0
    for sv in ds:
        if(sv.tensv.endswith("Lan")):
            count+=1
    return count
print("Số sinh viên tên Lan:", find_sv_lan(ds_dv))

#g.	Cho biết trong mảng có bao nhiêu sinh viên có họ «Phan»
def count_sv_hophan(ds):
    count =0
    for sv in ds:
        if(sv.tensv.startswith("Phan")):
            count+=1
    return count
print("Số sinh viên họ Phan:", count_sv_hophan(ds_dv))

# IV. Bài tập về nhà
# 1.	Viết hàm trộn 2 mảng một chiều thành 1 mảng một chiều với mỗi phần tử của mảng mới là min của 2 phần tương ứng từ 2 mảng cho trước. Trong quá trình trộn 2 mảng nếu mảng nào còn phần tử thì các phần tử còn lại của mảng đó sẽ đưa vào mảng mới. 
# Ví dụ: 
# Mảng a: 3 9 1 4 
# Mảng b: 2 7 4 3 2 8 
# Mảng kết quả: 2 7 1 3 2 8

def tron_mang():
    a=[]
    b=[]
    #nhập số phần tử của a và b
    n = int(input("Nhập số phần từ mãng a:"))
    m = int(input("Nhập số phần từ mãng b:"))
    for i in range(n):
        a.append(random.randint(0,99))
    for i in range(m):
        b.append(random.randint(0,99))
    print("Mảng a:", a)
    print("Mảng b:", b)

    #tìm độ dài mãng lớn nhất
    maxlen=0
    if(m>n):
        maxlen=m
    else:
        maxlen=n
    #chuổi mới
    c=[]
    for i in range(maxlen):
        if i<len(a) and i< len(b):
            c.append(min(a[i],b[i]))
        elif i< len(a):
            c.append(a[i])
        elif i < len(b):
            # chỉ còn phần tử trong b
            c.append(b[i])
    print("Mảng kết quả:", c)
    return np.array(c)
tron_mang()


#bài 2.	Cho mảng 2 chiều a có m dòng, n cột chứa số nguyên, viết các hàm sau: 
def bai2_vn():
    #viết hàm tính mảng 2 chiều
    n = int(input("Nhập số dòng: "))
    m = int(input("Nhập số cột: "))
    a = []
    for i in range(n):
        row=[]
        for j in range(m):
            row.append(random.randint(0,99))
        a.append(row)
    arr= np.array(a)
    for row in a:
        print(row)
    
    #tính các phần tam giác trên của ma trận a kể cả đường chéo chính
    b = [
    [1, 2, -3],
    [-4, 5, 6],
    [7, -8, 9]
    ]
    s_tgtren=0
    for i in range(len(b)):
        for j in range(len(b[0])):
            if i<=j:
                s_tgtren+=b[i][j]
    print("tổng các phần tử của tam giác trên: ",s_tgtren)

    #b.	Chuyển các phần tử âm thành trị tuyệt đối của nó trong b. 
    b_1=copy.deepcopy(b)
    for i in range(len(b_1)):
        for j in range(len(b_1[0])):
            if(b_1[i][j]<0):
                b_1[i][j]= abs(b_1[i][j])
    print("đổi giá trị của các phần tử âm: ")
    for row in b_1:
        print(row)

    #c.	Thay các phần tử chẵn trong a bằng số nguyên x cho trước. 
    x=0
    b_2=copy.deepcopy(b)
    for i in range(len(b_2)):
        for j in range(len(b_2[0])):
            if(b_2[i][j]%2==0):
                b_2[i][j]=x

    print("Đổi các giá trị của các phần tử chẳn thành số đã cho trước")
    for row in b_2:
        print(row)
    #d.	Kiểm tra a có toàn chẵn không? 
    b_3=copy.deepcopy(b)
    ischan= True
    for i in range(len(b_3)):
        for j in range(len(b_3[0])):
            if(b_3[i][j]%2!=0):
                ischan = False
    if ischan== True:
        print("Mãng chẵn")
    else:
        print("Mãng không chẵn")
    for row in b_3:
        print(row)
    #e.	Cho ma trận vuông a cấp n, viết hàm kiểm tra a có đối xứng không. Biết rằng ma trận đối xứng là ma trận có a[i][j] = a[j][i].
    sym_matrix = [
    [1, 2, 3],
    [2, 4, 5],
    [3, 5, 6]
]

    isDoiXung = True
    for i in range(len(sym_matrix)):
        for j in range(len(sym_matrix)):
            if sym_matrix[i][j] != sym_matrix[j][i]:
                isDoiXung = False
                break
        if not isDoiXung:
            break

    if isDoiXung:
        print("Mảng đối xứng")
    else:
        print("Mảng không đối xứng")
    #f.	Kiểm tra ma trận vuông a cấp n có đường chéo chính tăng dần không? 
    b_4=copy.deepcopy(b)
    istang = True
    for i in range(len(b_4)-1):
        if b_4[i][i] > b_4[i+1][i+1]:
                istang = False
                break
    if istang==True:
        print("Đường chéo chính tăng dần")
    else:
        print("Đường chéo chính không tăng dần")
    #g.	Xuất các phần tử thuộc tam giác dưới của đường chéo phụ kể cả đường chéo phụ trong ma trận vuông a cấp n. 
    print("Xuất các phần tử thuộc tam giác dưới của đường chéo phụ kể cả đường chéo phụ tỏng ma trận vuông a cấp n")
    b_5=copy.deepcopy(b)
    for i in range(len(b_5)):
        for j in range(len(b_5[0])):
            if i+j>=len(b)-1:
                print(b_5[i][j])
    #h.	Kiểm tra ma trận vuông a cấp n có đường chéo phụ giảm dần không?
    print("kiểm tra ma trận vuông a cấp n có đường chéo ohuj giảm dần không")
    b_6=copy.deepcopy(b)
    isgiam=True
    for i in range(len(b_6)-1):
        for j in range(len(b_6[0])-1):
            if i+j==len(b_6)-1:
                if b_6[i][j] <b_6[i+1][j+1]:
                    isgiam=False
    if isgiam==True:
        print("Đường chéo phụ giảm dần")
    else:
        print("Đường chéo phụ không không dần")
bai2_vn()

#Bài 3.	Tạo một dictionary chứa 3 dictionaries.
dict1 = {
    "Brand":"Mec",
    "Food":"Hot",
    "Year":1999,
    "Color":["red","cyan","blue"]
}
print(dict1)
# Mở file ở chế độ đọc ('r')
with open("data.txt", "r", encoding="utf-8") as f:
    content = f.read()   # đọc toàn bộ nội dung
    print("Nội dung file:")
    print(content)
# Forensic Mini Quest - Challenge 1 Writeup

## Challenge Information

- Title: micro_drive
- Level: Beginner
- Category: Forensics
- Objective: Tim flag duoc giau trong thiet bi luu tru dang nho

## De bai

"This storage device is tiny, but it still hides something interesting."

## Muc tieu phan tich

Xac dinh file quan trong, trich xuat du lieu tu image, va tim flag theo dinh dang FLAG{...}.

## Buoc 1 - Khao sat du lieu ban dau

Sau khi giai nen challenge, thu muc co cac thanh phan dang chu y:

```text
__MACOSX/
micro_drive/
  ._micro_drive.iso
  ._micro_drive
  micro_drive.iso
```

Nhan xet:

- Thu muc __MACOSX va cac file bat dau bang ._ la metadata do macOS sinh ra.
- File can phan tich thuc te la micro_drive.iso.

## Buoc 2 - Xac minh dinh dang file

Kiem tra loai file:

```bash
file micro_drive.iso
```

Ket qua:

```text
ISO 9660 CD-ROM filesystem data 'CHAL_TINY_USB'
```

Ket luan: Day la mot image ISO hop le, co the trich xuat truc tiep.

## Buoc 3 - Tim dau hieu bang strings

Quet nhanh cac chuoi ky tu de tim manh moi:

```bash
strings micro_drive.iso | grep -i flag
```

Ket qua:

```text
FLAG.PNG;1
```

Phat hien: Trong ISO co tep anh ten FLAG.PNG.

## Buoc 4 - Trich xuat noi dung ISO

Dung 7z de extract:

```bash
7z x micro_drive.iso
```

Sau khi trich xuat thu duoc tep FLAG.PNG.

## Buoc 5 - Doc noi dung tep anh

Mo anh FLAG.PNG, flag hien thi truc tiep tren anh:

![FLAG image](FLAG.PNG)

```text
FLAG{hey_i_just_bought_a_usb}
```

## Final Flag

```text
FLAG{hey_i_just_bought_a_usb}
```

## Tong ket

Challenge nay kiem tra ky nang forensic co ban:

- Nhan dien file/chung tu khong lien quan (metadata macOS)
- Xac minh dinh dang image (ISO 9660)
- Tim manh moi nhanh bang strings
- Trich xuat du lieu tu image ma khong can mount

## Lessons Learned

- Khong phai luc nao file .iso cung can mount moi phan tich duoc.
- strings la cong cu nhanh va hieu qua de tim IOC/keyword.
- Nen loc bo file rac nhu __MACOSX va ._ truoc khi phan tich.

nhập khẩu  os
 yêu cầu nhập khẩu
nhập  codec



def  tao_thu_muc ( name ):
    hệ điều hành . mkdir ( tên )
    hệ điều hành . chdir ( tên )



def  luu_file ( url , stt ):
    tệp  =  codec . open ( 'file'  +  str ( stt ) +  '.html' , 'w' , 'utf8' )
    tập tin . ghi ( yêu cầu . lấy ( url ). văn bản )
    tập tin . đóng ()



def  luu_tat_ca_file ( history , so_luong_trang ):
    for ( stt , url_con ) trong  enumerate ( history ):
        if  stt  > =  so_luong_trang :
            phá vỡ
        luu_file ( url_con , stt )
        print ( f ' { stt }  { url_con } ' )


def  main ():
    tao_thu_muc ( 'thinhvv' )
    luu_file ( 'https://baomoi.com/' , 2 )


nếu  __name__  ==  "__main__" :
    main ()
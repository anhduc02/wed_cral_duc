 yêu cầu nhập khẩu
from  bs4  import  BeautifulSoup
nhập  lại



def  sua_url_goc ( url_goc ):
    nếu  url_goc [ - 1 ] ==  '/' :
        url_goc  =  url_goc [ 0 : - 1 ]
        trả về  url_goc
    khác :
        trả về  url_goc



def  tim_url_lien_quan ( url , url_goc ):
    url_tim_duoc  =  set ()
    liên kết  =  yêu cầu . get ( url )
    link_soup  =  BeautifulSoup ( link . text , 'html.parser' )
    results  =  link_soup ( 'a' , attrs = { 'href' : True })
    cho  tôi  trong  kết quả :
        a  =  i [ 'href' ]
        mau  =  f '^ { url_goc } [^? #] * $'
        mau2  =  '^ / [^? #] * $'
        nếu  lại . khớp ( mau , a ):
            url_tim_duoc . thêm ( a )
        khác :
            nếu  lại . khớp ( mau2 , a ):
                url_lien_quan  =  f ' { url_goc } { a } '
                url_tim_duoc . thêm ( url_lien_quan )
    trả về  url_tim_duoc



def  them_va_duyet_hang_cho ( hang_cho , url_goc , so_luong_trang ):
    history  =  hang_cho
    while ( len ( hang_cho ) >  0 ) and ( len ( history ) <  so_luong_trang ):
        url_tim_duoc  =  tim_url_lien_quan ( hang_cho . pop (), url_goc )
        hang_cho  =  hang_cho  | ( url_tim_duoc  -  lịch sử )
        history  =  lịch sử  |  url_tim_duoc
     lịch sử trở lại


def  main ():
    url_tim_duoc  =  tim_url_lien_quan ( 'https://vietnamnet.vn' , 'https://vietnamnet.vn' )
    history  =  them_va_duyet_hang_cho ( url_tim_duoc )
    đối với  tôi  trong  lịch sử :
        in ( i )


nếu  __name__  ==  '__main__' :
    main ()
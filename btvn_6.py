import streamlit as st
import pandas as pd
from PIL import Image
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import matplotlib.pyplot as plt
import seaborn as sns
import base64
st.set_option('deprecation.showPyplotGlobalUse', False)

def add_bg_from_local(image_file):
    with open(image_file, "rb") as file:
        encoded_image = base64.b64encode(file.read()).decode("utf-8")
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url('data:image/jpeg;base64,{encoded_image}');
            background-repeat: no-repeat;
            background-position: center;
            background-size: cover;
        }}
        .stApp > div {{
            background-color: rgba(255, 255, 255, 0.8);
            padding: 20px;
            border-radius: 10px;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
add_bg_from_local('picture/background.jfif')
thanh_cong_cu = st.sidebar
with thanh_cong_cu:
    chon = st.radio("Bạn muốn tìm hiểu điều gì về Marvel?",('Thông tin cơ bản', 'Dòng thời gian và các sự kiện nổi bật', 'Những nhân vật nổi tiếng', 'Những dự án sắp tới', 'Đánh giá', 'Thống kê'))
st.markdown('<h1><center>Vũ trụ siêu anh hùng - MCU</center></h1>', unsafe_allow_html=True)
mcu = pd.read_excel('mcu.xlsx')
if chon == 'Thông tin cơ bản':
    st.markdown(f'<h2><center>{chon}</center></h2>', unsafe_allow_html=True)
    st.markdown('<h3>Marvel Studios là gì?</h3>', unsafe_allow_html=True)
    st.markdown('<p style="text-align: justify"><b>Marvel Studios</b> là một công ty sản xuất phim và truyền hình chuyên tạo ra những bộ phim hoặc chương trình siêu anh hùng dựa trên những nhân vật trong truyện tranh Marvel. Đây là một công ty con của Tập đoàn <i>The Walt Disney</i>. <b>Marvel Studios</b> đã sản xuất nhiều bộ phim cực kỳ thành công và phổ biến, bao gồm loạt phim <i>Avengers</i>, ba phần <i>Iron Man</i>, loạt phim <i>Captain America</i> và <i>Guardians of the Galaxy</i>. Các bộ phim của họ thường có cốt truyện và nhân vật liên kết với nhau, được gọi là <strong><i>Vũ trụ Điện ảnh Marvel (MCU)</i></strong>. Ngoài ra, <b>Marvel Studios</b> đã mở rộng sang lĩnh vực truyền hình với các chương trình như <i>Agents of S.H.I.E.L.D.</i> và <i>WandaVision.</i></p>', unsafe_allow_html=True)
    st.markdown('<h4>Thông tin liên hệ</h4>', unsafe_allow_html=True)
    st.markdown('Trang chủ: https://www.marvel.com/')
    st.markdown('Instagram: https://instagram.com/marvel/')
    st.markdown('Facebook: https://facebook.com/marvel/')
    st.markdown('Twitter: https://twitter.com/marvel/')
elif chon == 'Dòng thời gian và các sự kiện nổi bật':
    st.markdown(f'<h2><center>{chon}</center></h2>', unsafe_allow_html=True)
    nam = st.slider('Bạn muốn xem sự kiện của năm nào?', 2008, 2023, step=1)
    col_1, col_2 = st.columns(2)
    col_3, col_4 = st.columns(2)
    col_5, col_6 = st.columns(2)
    links = mcu['Info']
    if nam == 2008:
        with col_1:
            st.markdown(f'''<p style="text-align: justify"><a href={links[0]} title="Bộ phim">Iron Man</a>: Tony Stark, một tỷ phú thiên tài và nhà sản xuất vũ khí, trở thành Anh hùng Sắt sau khi bị bắt cóc và phát triển bộ giáp siêu năng.</p>''', unsafe_allow_html=True)        
        with col_2:  
            st.image('picture/Iron_Man.jfif', width = 300)
        with col_3:
            st.image('picture/Hulk.jfif', width = 300)
        with col_4:
            st.markdown(f'''<p style="text-align: justify"><a href={links[1]} title="Bộ phim">The Incredible Hulk</a>: Bruce Banner trở thành người khổng lồ xanh sau khi bị tác động bởi chất biến đổi và phải đối mặt với quá khứ và truy lùng.</p>''', unsafe_allow_html=True)
    elif nam == 2010:
        with col_1:
            st.markdown('''<p style="text-align: justify"><a href={links[2]} title="Bộ phim">Iron Man 2</a>: Tony Stark đối đầu với Ivan Vanko và suýt mất bộ giáp và công ty của mình.</p>''', unsafe_allow_html=True)        
        with col_2:  
            st.image('picture/Iron_Man_1.jfif', width = 300)
    elif nam == 2011:
        with col_1:
            st.markdown(f'''<p style="text-align: justify"><a href={links[3]} title="Bộ phim">Thor</a>: Thor trở thành người trần, mất quyền lực và phải học cách trở thành người tốt để lấy lại Mjolnir của mình.</p>''', unsafe_allow_html=True)        
        with col_2:  
            st.image('picture/Thor.jfif', width = 300)
        with col_3:
            st.image('picture/Captain_America.jfif', width = 300)
        with col_4:
            st.markdown(f'''<p style="text-align: justify"><a href={links[4]} title="Bộ phim">Captain America: The First Avenger</a>: Steve Rogers trở thành Captain America, người anh hùng mang biểu tượng của Mỹ và chiến đấu chống lại Red Skull trong Thế chiến II.</p>''', unsafe_allow_html=True)
    elif nam == 2012:
        with col_3:
            st.image('picture/Avengers.jfif', width = 300)
        with col_4:
            st.markdown(f'''<p style="text-align: justify"><a href={links[5]} title="Bộ phim">The Avengers</a>: Iron Man, Captain America, Thor, Hulk, Black Widow, Hawkeye hợp tác để ngăn chặn Loki và đội quân Chitauri xâm lược Trái Đất.</p>''', unsafe_allow_html=True)
    elif nam == 2013:
        with col_1:
            st.markdown(f'''<p style="text-align: justify"><a href={links[6]} title="Bộ phim">Iron Man 3</a>: Tony Stark chiến đấu với Mandarin và phải đối mặt với quá khứ cùng sự lo lắng cá nhân.</p>''', unsafe_allow_html=True)        
        with col_2:  
            st.image('picture/Iron_Man_2.jfif', width = 300)
        with col_3:
            st.image('picture/Thor_1.jfif', width = 300)
        with col_4:
            st.markdown(f'''<p style="text-align: justify"><a href={links[7]} title="Bộ phim">Thor: The Dark World</a>: Thor ngăn chặn Malekith và đối mặt với việc mất mát trong gia đình.</p>''', unsafe_allow_html=True)
    elif nam == 2014:
        with col_1:
            st.markdown(f'''<p style="text-align: justify"><a href={links[8]} title="Bộ phim">Captain America: The Winter Soldier</a>: Captain America phát hiện S.H.I.E.L.D. đã bị xâm phạm và phải đối đầu với Winter Soldier.</p>''', unsafe_allow_html=True)        
        with col_2:  
            st.image('picture/Captain_America_1.jfif', width = 300)
        with col_3:
            st.image('picture/Guardians of the Galaxy.jfif', width = 300)
        with col_4:
            st.markdown(f'''<p style="text-align: justify"><a href={links[9]} title="Bộ phim">Guardians of the Galaxy</a>: Peter Quill, Gamora, Rocket, Groot cùng Drax thành lập Guardians of the Galaxy để ngăn chặn Ronan và Thanos.</p>''', unsafe_allow_html=True)
    elif nam == 2015:
        with col_1:
            st.markdown(f'''<p style="text-align: justify"><a href={links[10]} title="Bộ phim">Avengers: Age of Ultron</a>: Avengers tạo ra Ultron nhưng phải đối đầu với sự phản bội và khám phá sức mạnh của Wanda Maximoff.</p>''', unsafe_allow_html=True)        
        with col_2:  
            st.image('picture/Avengers_1.jfif', width = 300)
        with col_3:
            st.image('picture/Ant_Man.jfif', width = 300)
        with col_4:
            st.markdown(f'''<p style="text-align: justify"><a href={links[11]} title="Bộ phim">Ant-Man</a>: Scott Lang trở thành Ant-Man và tham gia cướp một công nghệ nguy hiểm.</p>''', unsafe_allow_html=True)
    elif nam == 2016:
        with col_1:
            st.markdown(f'''<p style="text-align: justify"><a href={links[12]} title="Bộ phim">Captain America: Civil War</a>: Cuộc nội chiến xảy ra giữa các siêu anh hùng khi họ tranh luận về việc quản lý và độc lập.</p>''', unsafe_allow_html=True)        
        with col_2:  
            st.image('picture/Captain_America_2.jfif', width = 300)
        with col_3:
            st.image('picture/Doctor_Strange.jfif', width = 300)
        with col_4:
            st.markdown(f'''<p style="text-align: justify"><a href={links[13]} title="Bộ phim">Doctor Strange</a>: Stephen Strange học cách sử dụng ma thuật và trở thành Sorcerer Supreme.</p>''', unsafe_allow_html=True)
    elif nam == 2017:
        with col_1:
            st.markdown(f'''<p style="text-align: justify"><a href={links[14]} title="Bộ phim">Guardians of the Galaxy Vol. 2</a>: Nhóm Guardians phải đối mặt với những nguy hiểm mới và tìm hiểu về quá khứ của Star-Lord.</p>''', unsafe_allow_html=True)        
        with col_2:  
            st.image('picture/Guardians of the Galaxy_1.jfif', width = 300)
        with col_3:
            st.image('picture/Spider_Man.jfif', width = 300)
        with col_4:
            st.markdown(f'''<p style="text-align: justify"><a href={links[15]} title="Bộ phim">Spider-Man: Homecoming</a>: Peter Parker đối mặt với Vulture và học cách trở thành người hùng thực thụ dưới sự hướng dẫn của Tony Stark.</p>''', unsafe_allow_html=True)
        with col_5:
            st.markdown(f'''<p style="text-align: justify"><a href={links[16]} title="Bộ phim">Thor: Ragnarok</a>: Thor ngăn chặn Ragnarok và đánh bại Hela, chị gái của mình.</p>''', unsafe_allow_html=True)        
        with col_6:  
            st.image('picture/Thor_2.jfif', width = 300)
    elif nam == 2018:
        with col_1:
            st.markdown(f'''<p style="text-align: justify"><a href={links[17]} title="Bộ phim">Black Panther</a>: T'Challa trở thành vị vua tiếp theo của Wakanda và đối mặt với việc bảo vệ ngôi vương cùng nguồn vibranium của Wakanda khỏi những thế lực đen tối.</p>''', unsafe_allow_html=True)        
        with col_2:  
            st.image('picture/Black_Panther.jfif', width = 300)
        with col_3:
            st.image('picture/Avengers_3.jfif', width = 300)
        with col_4:
            st.markdown(f'''<p style="text-align: justify"><a href={links[18]} title="Bộ phim">Avengers: Infinity War</a>: Avengers và đồng minh chiến đấu chống lại Thanos, người muốn sở hữu tất cả các viên Đá Vô Cực để tiêu diệt nửa dân số.</p>''', unsafe_allow_html=True)
        with col_5:
            st.markdown('''<p style="text-align: justify"><a href={links[19]} title="Bộ phim">Ant-Man and The Wasp</a>: Scott Lang và Hope van Dyne hợp tác để tìm kiếm Janet van Dyne nhằm ngăn chặn Ghost.</p>''', unsafe_allow_html=True)        
        with col_6:  
            st.image('picture/Ant_Man_1.jfif', width = 300)
    elif nam == 2019:
        with col_1:
            st.markdown('''<p style="text-align: justify"><a href={links[20]} title="Bộ phim">Captain Marvel</a>: Carol Danvers trở lại Trái Đất và phải đối mặt với kẻ thù lâu đời của cô.</p>''', unsafe_allow_html=True)        
        with col_2:  
            st.image('picture/Captain_Marvel.jfif', width = 300)
        with col_3:
            st.image('picture/Avengers_4.jfif', width = 300)
        with col_4:
            st.markdown('''<p style="text-align: justify"><a href={links[21]} title="Bộ phim">Avengers: Endgame</a>: Nhóm Avengers còn sống cố gắng đảo ngược tình thế để đánh bại Thanos một lần và mãi mãi.</p>''', unsafe_allow_html=True)
        with col_5:
            st.markdown('''<p style="text-align: justify"><a href={links[22]} title="Bộ phim">Spider-Man</a>: Far From Home: Peter Parker đối mặt với Mysterio rồi dần học cách vượt qua sự mất mát và trách nhiệm.</p>''', unsafe_allow_html=True)        
        with col_6:  
            st.image('picture/Spider_Man_1.jfif', width = 300)
    elif nam == 2021:
        with col_1:
            st.markdown('''<p style="text-align: justify"><a href={links[23]} title="Bộ phim">Black Widow</a>: Natasha Romanoff đối mặt với quá khứ của mình và gặp các đồng đội cũ trong cuộc chiến chống lại một thế lực nguy hiểm.</p>''', unsafe_allow_html=True)        
        with col_2:  
            st.image('picture/Black_Widow.jfif', width = 300)
        st.markdown('Hiện tại, MCU vẫn tiếp tục phát triển với nhiều dự án tiếp theo như <b><i>Spider-Man: No Way Home, Thor: Love and Thunder, Doctor Strange in the Multiverse of Madness</b></i> và nhiều hơn nữa. Đây chỉ là một tóm tắt ngắn gọn của MCU, và câu chuyện vẫn đang tiếp tục!', unsafe_allow_html=True)
    else:
        st.write('Chúng tôi đang cập nhật các sự kiện!')
elif chon == 'Những nhân vật nổi tiếng':
    st.markdown(f'<h2><center>{chon}</center></h2>', unsafe_allow_html=True)
    col_1, col_2, col_3, col_4 = st.columns(4)
    col_5, col_6, col_7, col_8 = st.columns(4)
    col_9, col_10, col_11, col_12 = st.columns(4)
    col_13, col_14, col_15, col_16 = st.columns(4)
    col_17, col_18, col_19, col_20 = st.columns(4)
    nhan_vat = ['Iron Man (Tony Stark)', 'Captain America (Steve Rogers)', 'Thor', 'Hulk (Bruce Banner)']
    nhan_vat_1 = ['Black Widow (Natasha Romanoff)', 'Hawkeye (Clint Barton)', 'Doctor Strange (Stephen Strange)', 'Spider-Man (Peter Parker)'] 
    nhan_vat_2 = ["Black Panther (T'Challa)", 'Captain Marvel (Carol Danvers)', 'Ant-Man (Scott Lang)', 'Wasp (Hope van Dyne)'] 
    nhan_vat_3 = ['Scarlet Witch (Wanda Maximoff)', 'Vision', 'Falcon (Sam Wilson)', 'Winter Soldier (Bucky Barnes)']
    nhan_vat_4 = ['Star-Lord (Peter Quill)', 'Gamora', 'Rocket Raccoon', 'Groot']
    hinh = ['Iron_Man_3.jfif', 'Captain_America_3.jfif', 'Thor_3.jfif', 'Hulk_1.jfif']
    hinh_1 = ['Black_Widow_1.jfif', 'Hawkeye.jfif', 'Doctor_Strange_1.jfif', 'Spider_Man_2.jfif'] 
    hinh_2 = ['Black_Panther_1.jfif', 'Captain_Marvel_1.jfif', 'Ant_Man_2.jfif', 'Wasp.jpg']
    hinh_3 = ['Wanda.jfif', 'Vision.jfif', 'Falcon.png', 'Winter_Soldier.jfif']
    hinh_4 = ['Star_Lord.jfif', 'Gamora.jfif', 'Rocket Raccoon.jfif', 'Groot.jfif']
    noi_dung = ['Iron Man là một siêu anh hùng hư cấu xuất hiện lần đầu trong truyện tranh được xuất bản bởi Marvel Comics, được tạo ra bởi nhà văn và biên tập viên Stan Lee, phát triển bởi biên kịch Larry Lieber và được thiết kế bởi các họa sĩ Don Heck và Jack Kirby. Nhân vật lần đầu xuất hiện trong tập truyện Tales of Suspense # 39 vào tháng 3 năm 1963. Iron Man tên thật là Tony Stark, một tỷ phú, nhà phát minh thiên tài và một người ăn chơi khét tiếng. Stark là chủ sở hữu của Stark Industries, một tập đoàn công nghiệp đa quốc gia chuyên sản xuất vũ khí. Sau khi bị thương nặng và bị bắt giữ bởi khủng bố, anh xây dựng một bộ giáp tiên tiến để thoát khỏi và duy trì cuộc sống của mình. Bộ giáp, được gọi là giáp Iron Man, cung cấp cho Stark sức mạnh siêu người, khả năng bay và một loạt vũ khí. Tony Stark sử dụng bộ giáp của mình để chiến đấu với tội phạm, bảo vệ dân thường vô tội và bảo vệ thế giới khỏi các siêu ác nhân khác nhau. Qua các năm, nhân vật này đã trở thành một trong những siêu anh hùng nổi tiếng nhất của Marvel. Iron Man đã xuất hiện trong nhiều loạt truyện tranh, chương trình truyền hình hoạt hình và trò chơi điện tử. Nhân vật cũng đã đạt được sự phổ biến đáng kể thông qua sự thể hiện của mình trong các bộ phim Vũ trụ Điện ảnh Marvel (MCU). Trí thông minh cùng nhân cách không hoàn hảo của nhân vật đã khiến anh trở thành một trong những người hâm mộ yêu thích. Iron Man thường được nhận xét là một trong những trụ cột của Vũ trụ Marvel và đã đóng một vai trò quan trọng trong nhiều cốt truyện lớn.', 
    'Captain America, hoặc còn được gọi là Đội trưởng Mỹ, là một nhân vật siêu anh hùng xuất hiện trong truyện tranh của Marvel Comics, được tạo ra bởi nhà văn Joe Simon và nghệ sĩ Jack Kirby, và lần đầu tiên xuất hiện trong Captain America Comics #1 vào năm 1941. Captain America là một nhân viên quân đội được tăng cường siêu năng lực bằng một loại huyết tương tạo ra từ thí nghiệm. Anh mang một chiếc khiên bằng kim loại đi kèm và là một võ sĩ xuất sắc. Captain America đã chống lại các thế lực xấu và bảo vệ nước Mỹ và tự do trên toàn thế giới. Nhân vật Steve Rogers là Captain America. Anh là một người lính quân đội tận tâm và luôn tin tưởng vào các giá trị đạo đức và công lý. Steve Rogers đã hy sinh bản thân để chiến đấu vì lợi ích chung và tiếp tục chiến đấu dưới trang phục Captain America trong nhiều thập kỷ. Anh là biểu tượng của sự can đảm, sự liêm chính và lòng yêu nước. Captain America đã trở thành một trong những nhân vật nổi tiếng nhất của Marvel. Anh đã xuất hiện trong nhiều bộ truyện tranh, loạt phim điện ảnh và chương trình truyền hình. Vai trò của Captain America trong Marvel Cinematic Universe (MCU) được thể hiện bởi diễn viên Chris Evans. Nhờ khả năng chiến đấu tuyệt vời, lòng trung thành và tình yêu cho nước Mỹ, Captain America đã trở thành một biểu tượng đáng kính và một trong những cột mốc quan trọng trong câu chuyện siêu anh hùng của Marvel.', 
    'Thor là một nhân vật siêu anh hùng xuất hiện trong truyện tranh của Marvel Comics. Nhân vật được tạo ra bởi nhà văn Stan Lee, biên kịch Larry Lieber và nghệ sĩ Jack Kirby, và lần đầu tiên xuất hiện trong Journey into Mystery #83 vào năm 1962. Thor là một Vệ thần, ban đầu  được biết đến là một vị thần trong thần thoại Bắc  u. Nhưng trong truyện tranh Marvel, Thor là một ánh sáng từ Asgard. Anh có sức mạnh phi thường, khả năng chiến đấu xuất sắc và sở hữu chiếc búa Mjolnir. Anh có thể sử dụng sức mạnh sét và điều khiển thời tiết. Mjolnir, chiếc búa của Thor, được chú trọng và chỉ người có tư cách đáng kính mới có thể sử dụng. Anh là con trai Ngự thần Odin, vị vua của Asgard. Thor là một chiến binh dũng cảm, can đảm và trung thành. Anh đã chiến đấu bên cạnh các Nhóm Vệ binh và Liên minh siêu anh hùng của Marvel để bảo vệ vũ trụ khỏi các mối đe dọa. Thor xuất hiện trong nhiều truyện tranh, loạt phim điện ảnh và chương trình truyền hình. Thành công của Thor đạt đỉnh cao với sự thể hiện của diễn viên Chris Hemsworth trong Marvel Cinematic Universe (MCU). Với sức mạnh phi thường và tình yêu cho công lý, Thor là một trong những nhân vật đáng nhớ nhất của Marvel. Anh là biểu tượng của sức mạnh và thành công, cũng như lòng trung thành và cống hiến.', 
    'Hulk là một nhân vật siêu anh hùng xuất hiện trong truyện tranh của Marvel Comics, được tạo ra bởi nhà văn Stan Lee và nghệ sĩ Jack Kirby và lần đầu tiên xuất hiện trong The Incredible Hulk #1 vào năm 1962. Hulk là hình dạng biến đổi của nhà khoa học Bruce Banner sau khi anh bị tia gamma tác động trong một thí nghiệm. Đặc điểm nổi bật của Hulk là sức mạnh vô đối và khả năng tự chữa lành nhanh chóng. Khi trở thành Hulk, Bruce Banner trở thành một con quái vật màu xanh to lớn, mạnh mẽ và khó kiểm soát. Hulk là biểu tượng của sức mạnh tàn phá và cơn giận. Anh có thể làm bẹp vá, phá hủy và ném vật thể với sức mạnh phi thường. Tuy nhiên, Hulk cũng có một phần con người bên trong Bruce Banner, và câu chuyện xoay quanh việc cân bằng và điều khiển cả hai khía cạnh này. Bruce Banner thường cố gắng kiềm chế sự biến đổi thành Hulk để đảm bảo an toàn cho những người xung quanh. Hulk đã xuất hiện trong nhiều truyện tranh, loạt phim điện ảnh và chương trình truyền hình. Trong Marvel Cinematic Universe (MCU), Mark Ruffalo đã đóng vai Bruce Banner/Hulk. Với sức mạnh và thế lực phi thường, Hulk là một trong những nhân vật nổi tiếng nhất và đáng nhớ nhất của Marvel. Anh biểu thị cho sự tranh đấu, lòng dũng cảm và sức mạnh phi thường trong cuộc chiến chống lại các siêu ác nhân và bảo vệ công lý.']
    noi_dung_1 = ['Black Widow là một nhân vật siêu anh hùng trong truyện tranh và Marvel Cinematic Universe (MCU) của Marvel. Natasha Romanoff, còn được gọi là Black Widow, là một đặc vụ tình báo và một chiến binh tài ba. Black Widow là một nhân vật cực kỳ đa tài và có nhiều kỹ năng chiến đấu, bao gồm các kỹ thuật quyền đấm, quyền đá, võ thuật, sử dụng vũ khí và chiến lược. Cô cũng là một hacker giỏi và có khả năng trộn lẫn vào môi trường với sự mạnh dạn và sự phối hợp. Black Widow không có siêu năng lực nổi bật, nhưng lại được ghi nhận với sự sắc bén trong thái độ chiến đấu và trí thông minh tấn công. Cô có sức mạnh về tâm lý và tổ chức. Câu chuyện của Black Widow tập trung vào quá khứ đen tối của cô và quyết định của cô trở thành một anh hùng. Natasha Romanoff, trước đây là một điệp viên của KGB, sau khi gặp và làm việc với S.H.I.E.L.D, cô đã trở thành thành viên chính thức của đội Avengers. Black Widow là một thành viên quan trọng trong Liên minh siêu anh hùng và có nhiều đóng góp quan trọng trong việc chiến đấu chống lại các mối đe dọa và bảo vệ thế giới. Black Widow đã xuất hiện trong nhiều bộ truyện tranh, loạt phim điện ảnh và chương trình truyền hình. Scarlett Johansson đã đóng vai Black Widow trong MCU và đã thể hiện tài năng của mình trong các phần Avengers và các bộ phim solo của Black Widow. Với sự thông minh, sự linh hoạt và lòng dũng cảm, Black Widow là một nhân vật siêu anh hùng quan trọng và đáng nhớ trong vũ trụ Marvel. Cô là biểu tượng của sự can đảm, sự sắc bén và tình yêu cho công lý.',
    'Hawkeye là một nhân vật siêu anh hùng trong Marvel Cinematic Universe (MCU). Tên thật của Hawkeye là Clint Barton và anh là một xạ thủ xuất sắc. Hawkeye được biết đến với khả năng bắn cung tuyệt vời và kỹ năng đánh đòn chính xác. Anh có thể bắn cung một cách chính xác và tạo ra những đòn trúng tiếng với mọi đối thủ. Hawkeye cũng là một võ sĩ tài ba với kỹ năng chiến đấu gần gũi và tầm xa. Clint Barton trước đây là một lính đánh thuê, sau đó gia nhập Liên quân S.H.I.E.L.D và trở thành một thành viên chính của đội Avengers. Hawkeye đã có nhiều đóng góp quan trọng trong việc đối phó với các mối đe dọa và bảo vệ thế giới bên cạnh các siêu anh hùng khác. Hawkeye không có siêu năng lực siêu phàm, nhưng anh đã rèn luyện kỹ năng mình đến đỉnh cao và trở thành một chiến binh đáng gờm. Anh có khả năng quan sát tinh tường và chiến đấu tinh vi. Hawkeye cũng sử dụng các công nghệ hiện đại và vũ khí tiên tiến để làm nổi bật sức mạnh của mình. Nhân vật Hawkeye đã xuất hiện trong nhiều truyện tranh, loạt phim điện ảnh và chương trình truyền hình. Trong MCU, Jeremy Renner đã đóng vai Hawkeye và đã thể hiện được tài năng của mình trong các phần Avengers và các bộ phim solo của Hawkeye. Với sự khéo léo, sự chính xác và lòng dũng cảm, Hawkeye là một nhân vật siêu anh hùng quan trọng và đáng nhớ trong vũ trụ Marvel. Anh biểu thị cho sự kiên nhẫn, kỹ năng và lòng trung thành để bảo vệ công lý và chiến đấu chống lại các mối đe dọa.',
    'Doctor Strange là một nhân vật siêu anh hùng trong Marvel Cinematic Universe (MCU) của Marvel. Tên thật của Doctor Strange là Stephen Strange, và anh là một bác sĩ phẫu thuật giỏi và nổi tiếng. Doctor Strange nổi tiếng với khả năng sử dụng phép thuật và ma thuật để chiến đấu với các mối đe dọa siêu nhiên. Anh đã học tại Kamar-Taj, một ngôi trường đào tạo phù thủy tại xứ sở Tibet, và trở thành Mặt Trời Tiên Tri - Người giữ giấy phép Phép Thuật lớn nhất trong vũ trụ. Với việc sử dụng các kỹ thuật phù thuỷ, Doctor Strange có thể thay đổi thực tế, đi xuyên qua không gian và thời gian, tạo ra các cuộc tấn công phép thuật mạnh mẽ và sử dụng ma pháp trong việc chữa trị và phục hồi sức khỏe. Anh cũng có khả năng đấu lại các thế lực siêu nhiên và thám thích Cảnh cáo về các sự kiện nguy hiểm. Doctor Strange là một nhân vật có tính cách kiêu ngạo và tự nhận mình là một người thông minh. Tuy nhiên, sau khi bị tai nạn xe hơi và mất khả năng làm việc với tay, ông đã tìm đến thế lực siêu nhiên để tìm kiếm sự phục hồi và lợi ích trong việc chiến đấu chống lại sự ác và bảo vệ thế giới. Nhân vật Doctor Strange đã xuất hiện trong nhiều loạt truyện tranh và đã có bộ phim riêng mang tên Doctor Strange ra mắt vào năm 2016 trong MCU. Trong bộ phim này, Benedict Cumberbatch đóng vai Doctor Strange và đã thể hiện sự phong cách độc đáo và bề dày diễn xuất của mình. Với sự thông minh, khả năng phép thuật và quả cảm, Doctor Strange là một nhân vật siêu anh hùng quan trọng và đáng nhớ trong vũ trụ Marvel. Anh biểu thị cho trí tuệ, lòng can đảm và khả năng chiến đấu với những kẻ ác và bảo vệ thế giới.',
    'Spider-Man là một nhân vật siêu anh hùng trong truyện tranh và Marvel Cinematic Universe (MCU) của Marvel. Tên thật của Spider-Man là Peter Parker, một học sinh trung học thông thường, bị cắn bởi một con nhện phóng xạ và nhận được các siêu năng lực nhện. Ngay sau cú cắn, Peter Parker phát triển sức mạnh, tốc độ, độ linh hoạt và khả năng bám vào tường tương tự như các loài nhện. Ngoài ra, anh còn có cảm giác nhạy bén. Spider-Man được biết đến với tinh thần nghĩa hiệp, lòng dũng cảm và nguyện vọng bảo vệ người dân vô tội khỏi bất kỳ nguy hiểm nào. Nhân vật huyền thoại này đã trở thành một biểu tượng về sự trách nhiệm và lòng chung thủy đối với chiến đấu bảo vệ công lý. Spider-Man đã xuất hiện trong nhiều  truyện tranh, loạt phim điện ảnh và chương trình truyền hình. Anh đã trở thành nhân vật phổ biến nhất của Marvel và được yêu thích rộng rãi trên toàn thế giới. Spider-Man đã được thể hiện bởi một số diễn viên khác nhau trong các bộ phim MCU, bao gồm Tobey Maguire, Andrew Garfield và Tom Holland. Spider-Man là một nhân vật siêu anh hùng quan trọng và đáng nhớ trong vũ trụ Marvel. Anh ta biểu thị cho sự trí tuệ, sức mạnh vượt trội, lòng dũng cảm trong việc đương đầu với sự nguy hiểm và bảo vệ người dân vô tội.']
    noi_dung_2 = ["Black Panther là một nhân vật siêu anh hùng trong Marvel Cinematic Universe (MCU) của Marvel. Tên thật của Black Panther là T'Challa, và anh là vị vua và siêu anh hùng của Wakanda, một quốc gia ẩn lạc phụ thuộc vào công nghệ tiên tiến và khoáng sản quý. Black Panther nổi tiếng với bộ áo cơ thể bọc kim tiêm chiết xuất từ Vibranium, chất chống đạn mạnh mẽ. Với bộ áo này, T'Challa có sức mạnh, tốc độ, linh hoạt và khả năng chống lại các cuộc tấn công. Anh cũng là một chiến binh lỗi lạc với kỹ thuật võ thuật cao cấp và khả năng chiến đấu gần gũi cùng tầm xa. Ngoài ra, T'Challa còn là vị vua của Wakanda, điều hành quốc gia với sự khéo léo và lòng trung thành. Không chỉ là một người hùng, anh còn phải đối mặt với các thách thức và trách nhiệm của vị trí vua. Black Panther là một biểu tượng về tổ chức, lòng can trường và lòng xã hội. Nhân vật này không chỉ đại diện cho quyền lực và sức mạnh cá nhân, mà còn đề cao tình yêu quê hương. Black Panther đã xuất hiện trong nhiều loạt truyện tranh và đã có một bộ phim riêng mang tên Black Panther được phát hành vào năm 2018. Trong bộ phim này, Chadwick Boseman đóng vai Black Panther và đã thể hiện sự khéo léo cùng tài năng của mình. Black Panther là một nhân vật siêu anh hùng quan trọng và đáng nhớ trong vũ trụ Marvel. Anh biểu thị cho sự công bằng, lòng yêu thương, sức mạnh con người trong việc xây dựng và bảo vệ quốc gia của mình.",
    'Captain Marvel là một nhân vật siêu anh hùng trong Marvel Cinematic Universe (MCU). Tên thật của Captain Marvel là Carol Danvers, và cô là một phi công, điều tra viên quân đội trước khi nhận được siêu năng lực đắt giá. Carol Danvers đã bị tia năng lượng của một công trình không gian phục hồi mà không thể giải thích xuyên qua cơ thể, biến đổi cấu trúc di truyền của cô và trao cho cô sức mạnh siêu nhiên. Cô có sức mạnh, tốc độ, linh hoạt và khả năng bay có thể so sánh với các siêu anh hùng mạnh nhất trong vũ trụ Marvel. Captain Marvel cũng có thể xả ra các vụ nổ năng lượng. Cô có thể đi qua không gian và thời gian một cách nhanh chóng. Khi vì mục tiêu của cô và công lý, Captain Marvel không ngần ngại trong việc chiến đấu chống lại các mối đe dọa siêu nhiên. Captain Marvel đã xuất hiện trong nhiều loạt truyện tranh và đã có một bộ phim riêng mang tên Captain Marvel ra mắt vào năm 2019 trong MCU. Trong bộ phim này, Brie Larson đóng vai Captain Marvel và đã thể hiện sự sáng tạo và tài năng của mình. Với sự mạnh mẽ, sự chiến đấu và ý chí vững chắc, Captain Marvel là một nhân vật siêu anh hùng quan trọng và đáng nhớ trong vũ trụ Marvel. Cô biểu thị cho sự tự do, sức mạnh, công lý trong việc bảo vệ vũ trụ khỏi các mối đe dọa siêu nhiên, và là một biểu tượng sự mạnh mẽ và quyền lực của phụ nữ.', 
    'Ant-Man là một nhân vật siêu anh hùng trong Marvel Cinematic Universe (MCU) của Marvel. Ant-Man tên thật là Scott. Anh có thể giảm kích thước để trở thành Ant-Man và tăng kích thước để trở thành Ant-Man khổng lồ. Anh cũng có sức mạnh và linh hoạt kéo dài từ kích thước bé nhỏ đến kích thước lớn. Ngoài việc có khả năng đi qua những khoảng không gian nhỏ và vượt qua các rào cản, Ant-Man cũng có khả năng tương tác với kiến, dẻ hoặc hoặc bất kỳ sinh vật nhỏ nào. Điều này cho phép Ant-Man có những khả năng độc đáo và khó lường trong việc chiến đấu và thực hiện các nhiệm vụ. Ant-Man là một nhân vật siêu anh hùng có tính cách hài hước và thích phiêu lưu. Với sự điềm đạm và trí tuệ của mình, Ant-Man giúp tạo ra các kế hoạch thông minh và giải quyết các vấn đề bằng cách sử dụng sức mạnh của mình. Ant-Man đã xuất hiện trong nhiều loạt truyện tranh và có hai phần phim riêng mang tên "Ant-Man" và "Ant-Man and the Wasp" trong MCU. Anh biểu thị cho sự sáng tạo và sẵn sàng vượt qua các thách thức với thái độ tích cực và hài hước.', 
    'Wasp là một nhân vật siêu anh hùng trong truyện tranh và Marvel Cinematic Universe (MCU) của Marvel. Tên thật của Wasp là Hope van Dyne. Wasp có khả năng điều khiển vi mô, giống như Ant-Man. Cô có thể giảm kích thước của mình để trở thành một người nhỏ bé, và sử dụng cánh và chiến thuật chiến đấu tốc độ cao. Wasp cũng có thể tạo ra hàng loạt lượng năng lượng tưởng tượng từ cơ thể mình, cho phép cô tạo ra vũ trụ năng lượng và tia năng lượng. Wasp có khả năng bay rất nhanh và linh hoạt trong không gian nhỏ. Cô cũng có cánh cùng sợi kiến để tăng cường chiến thuật và vận động. Bên cạnh đó, Wasp cũng đã được đào tạo trong võ thuật và chiến đấu, điều này giúp cô trở thành một chiến binh vượt trội. Với sự thông minh, sự linh hoạt và khả năng chiến đấu chưa từng thấy của mình, Wasp là một nhân vật siêu anh hùng đáng chú ý trong vũ trụ Marvel. Cô biểu thị sự quyết tâm và động lực nhằm bảo vệ thế giới khỏi các mối đe dọa siêu nhiên. Wasp đã xuất hiện trong nhiều truyện tranh và trong các bộ phim trong MCU, bao gồm "Ant-Man and the Wasp". Trong phim này, Evangeline Lilly đã đóng vai Wasp.']
    noi_dung_3 = ['Scarlet Witch hay còn được gọi là Wanda Maximoff là một nhân vật siêu anh hùng trong truyện Marvel Cinematic Universe. Cô là một người phụ nữ có khả năng siêu nhiên mạnh mẽ và có thể điều khiển năng lượng phép thuật. Scarlet Witch có khả năng tạo ra cũng như điều khiển năng lượng phép thuật, cho phép cô thực hiện các hành động như tạo ra cột lửa, phá vỡ vật thể, hoặc thay đổi thời gian và không gian. Cô cũng có khả năng đọc suy nghĩ và chi phối ý chí của người khác. Ngoài ra, Scarlet Witch cũng có khả năng tạo ra các trường năng lượng bảo vệ và tăng cường sức mạnh của mình. Cô có thể tẩu thoát khỏi hiểm nguy và thực hiện các đòn tấn công mạnh mẽ để chống lại kẻ thù. Scarlet Witch đã có một hành trình phát triển đáng chú ý trong MCU. Ban đầu, cô được giới thiệu như một nhân vật có khả năng phép thuật mạnh mẽ nhưng chưa thể kiểm soát hoàn toàn. Sau đó, cô đã trải qua quá trình đào tạo và thành thạo hơn trong việc sử dụng khả năng của mình. Scarlet Witch là một nhân vật có tính cách phức tạp và đã trải qua nhiều khó khăn và mất mát trong cuộc sống. Cô biểu thị sự kiên nhẫn và quyết tâm trong việc đối mặt với sự thất vọng và khám phá bản thân mình.',
    'Vision là một nhân vật siêu anh hùng trong Marvel Cinematic Universe (MCU)l. Anh là một trong những thành viên quan trọng của nhóm Avengers. Vision ban đầu được tạo ra bởi Ultron, một trí tuệ nhân tạo tàn ác, nhưng sau đó anh trở thành một đồng minh và thành viên của Avengers. Khi được tạo ra, Vision đã thuần hóa bởi Mind Stone, một trong sáu viên đá Vô cực mạnh mẽ trong MCU. Viên đá này đã cung cấp cho Vision sức mạnh và năng lực phi thường. Vision có thể bay, có sức mạnh vô địch và khả năng chiến đấu vô cùng tài ba. Anh cũng có khả năng đồng hóa vật liệu của mình, cho phép anh thông qua và thao tác qua các vật thể rắn hoặc đi qua các vật thể rỗng. Ngoài ra, Vision còn có khả năng phân tích, xử lý thông tin nhanh chóng, giúp anh hiểu rõ về thế giới xung quanh và đưa ra quyết định thông minh. Anh cũng có khả năng phóng laser từ trán và sử dụng sức mạnh của Mind Stone để tạo ra các vụ nổ năng lượng mạnh mẽ. Mặc dù Vision là một trí tuệ nhân tạo, nhưng anh có tình cảm và ý thức riêng. Anh đóng vai trò như một người gương lý tưởng, luôn muốn thực hiện sứ mệnh bảo vệ và cứu giúp những người yếu đuối. Vision đã xuất hiện trong nhiều truyện tranh và trong các bộ phim trong MCU, bao gồm "The Avengers" và "Avengers: Infinity War". Trong MCU, Paul Bettany đóng vai Vision.',
    'Falcon, hay còn được gọi là Sam Wilson, là một nhân vật siêu anh hùng trong Marvel Cinematic Universe. Anh đã xuất hiện trong các bộ phim như "Captain America: The Winter Soldier", "Avengers: Age of Ultron", "Captain America: Civil War" và các bộ phim Avengers sau này. Falcon ban đầu xuất hiện như là một cựu binh Chiến tranh Việt Nam có kỹ năng phi công hàng không. Anh đã nhận được bộ trang bị đặc biệt được gọi là "EXO-7 Falcon", cho phép anh bay và sử dụng các vũ khí công nghệ cao. Bộ cánh Falcon cung cấp cho anh khả năng bay qua không trung và tốc độ cao. Anh cũng sử dụng một số vũ khí như súng và pháo cơ đặc biệt. Ngoài khả năng bay và chiến đấu, Falcon cũng là một chiến binh tài ba và có kỹ năng chiến đấu chuyên nghiệp. Anh đã được huấn luyện trong các kỹ thuật võ thuật và quân sự, làm cho anh trở thành một thành viên quan trọng của nhóm Avengers. Falcon cũng có tình cảm và lòng trung thành với bạn bè và những người anh em. Anh đã trở thành một người đồng đội đáng tin cậy giúp đỡ trong nhiều cuộc phiêu lưu và chiến tranh của Avengers. Người đóng vai Falcon trong MCU là Anthony Mackie. Falcon đã trở thành một nhân vật phổ biến và được yêu thích trong vũ trụ Marvel nhờ kỹ năng đặc biệt và tấm lòng can đảm của mình. Falcon biểu thị sự quyết tâm và sự kiên nhẫn trong việc bảo vệ công lý và chiến đấu cho công cuộc tốt đẹp hơn. Với khả năng bay, chiến đấu tài ba và tâm hồn anh hùng, Falcon là một nhân vật siêu anh hùng đáng chú ý trong vũ trụ Marvel.',
    'Winter Soldier hay còn được gọi là Bucky Barnes là một nhân vật siêu anh hùng trong Marvel Cinematic Universe (MCU) của Marvel. Anh đã xuất hiện trong các bộ phim như "Captain America: The Winter Soldier", "Captain America: Civil War" và "Avengers: Infinity War". Trước đây, Bucky Barnes là một người lính trong Chiến tranh thế giới thứ hai và bạn thân của Steve Rogers, còn được biết đến với tên gọi Captain America. Tuy nhiên, trong một sự kiện không may, Bucky bị mất tích và bị xem là đã chết. Bucky sau đó trở thành Winter Soldier, một sát thủ với kỹ năng vũ khí cao cấp và siêu năng lực. Anh đã bị cải tạo và kiểm soát bởi tổ chức Hydra, trở thành một công cụ giết người không độc lập. Sau khi Captain America tìm được Bucky và giúp anh nhớ lại quá khứ, Winter Soldier đã trở thành một nhân vật có tâm hồn phức tạp, đấu tranh để tìm kiếm sự cải tạo và chuộc tội cho những tội ác mà anh phạm. Bucky Barnes có khả năng chiến đấu chuyên nghiệp và sử dụng các vũ khí như súng và dao. Anh cũng có siêu sức mạnh và sự phục hồi nhanh chóng. Mặc dù anh đã trải qua nhiều biến cố và thách thức trong cuộc sống, Bucky đã trở thành một người bạn đồng hành đáng tin cậy và anh hùng. Sebastian Stan vào vai Winter Soldier trong MCU và đã tạo nên một nhân vật đầy cảm xúc và phức tạp. Tự do và sự trở lại trong vai trò người hùng đã giúp Bucky tìm lại đạo đức và mục tiêu trong cuộc sống.',]
    noi_dung_4 = ['Star-Lord hay còn được gọi là Peter Quill là một nhân vật siêu anh hùng trong Marvel Cinematic Universe. Anh đã xuất hiện trong các bộ phim như "Guardians of the Galaxy" và "Avengers: Infinity War". Star-Lord là một phi hành gia và trộm tinh vi. Anh là người lãnh đạo của Guardians of the Galaxy, một nhóm siêu anh hùng hỗn hợp bao gồm các thành viên khác như Gamora, Drax, Rocket và Groot. Peter Quill có khả năng chiến đấu bằng các vũ khí như súng và dao, và anh cũng cơ động và khéo léo trong việc di chuyển và đối phó với các tình huống nguy hiểm. Peter Quill có một vật phẩm đặc biệt là chiếc tai nghe Walkman, chứa danh sách nhạc quý giá từ trái đất. Nhạc là một phần quan trọng trong cuộc sống của Star-Lord và đã xuất hiện trong nhiều phân cảnh quan trọng của các bộ phim Guardians of the Galaxy. Star-Lord có tính cách hài hước, đôi khi lém lĩnh và tinh nghịch. Anh cũng có tấm lòng tốt và cam kết bảo vệ các thành viên trong nhóm Guardians of the Galaxy. Chris Pratt vào vai Star-Lord trong MCU và đã tạo nên một nhân vật hài hước và đáng yêu. Sự phiêu lưu và hành trình của Star-Lord đã góp phần quan trọng vào câu chuyện lớn của MCU.',
    'Gamora là một nhân vật siêu anh hùng trong truyện tranh và Marvel Cinematic Universe (MCU) của Marvel. Cô đã xuất hiện trong các bộ phim như "Guardians of the Galaxy", "Guardians of the Galaxy Vol. 2" và "Avengers: Infinity War". Gamora là một nhân vật nữ mạnh mẽ và tàn nhẫn. Cô là con gái của Thanos và đã được huấn luyện thành một sát thủ chuyên nghiệp. Gamora trở thành một thành viên Quý Ngũ Hùng (Guardians of the Galaxy) và là một trong những nhân vật chính trong nhóm. Gamora có sức mạnh và khả năng chiến đấu vượt trội. Cô là một chiến binh tài ba và sở hữu kỹ thuật võ thuật cao cấp. Gamora cũng sử dụng các vũ khí như dao và súng để chiến đấu. Mặc dù lớn lên dưới sự điều khiển của Thanos, Gamora đã trở nên phản đối và cố gắng chống lại sự ám muội của cha mình. Cô dần dần trở thành một người hùng và bảo vệ vũ trụ khỏi các mối đe dọa. Gamora được đóng vai bởi nữ diễn viên Zoe Saldana trong MCU. Cô đã tạo nên một nhân vật mạnh mẽ và lôi cuốn, với cảm xúc sâu sắc và quyết tâm chiến đấu cho công lý. Gamora đã trở thành một trong những nhân vật được yêu thích nhất trong vũ trụ Marvel nhờ sự mạnh mẽ và lòng can đảm của mình. Cô đại diện cho sự cứng rắn và ý chí kiên cường trong việc đối mặt với sự ác độc và tìm kiếm sự cân bằng giữa sự trừng phạt và sự tha thứ.',
    'Rocket Raccoon là một nhân vật siêu anh hùng trong Marvel Cinematic Universe. Anh đã xuất hiện trong các bộ phim như "Guardians of the Galaxy", "Guardians of the Galaxy Vol. 2" và "Avengers: Endgame". Rocket Raccoon là một con rái cá thông minh dẫn đầu công việc của mình như một sát thủ và hacker. Rocket Raccoon có thông minh vượt trội và sở hữu khả năng dùng các loại vũ khí hiện đại. Anh là chuyên gia trong việc sửa chữa máy móc và đánh lừa hệ thống an ninh. Rocket Raccoon cũng có khả năng chiến đấu với các kỹ năng bắn súng và cắt đứt. Mặc dù có vẻ bề ngoài nhỏ bé và dễ thương, Rocket Raccoon có tính cách nóng nảy và thô lỗ. Anh thường thể hiện sự khó chịu và khích bác đối với mọi người xung quanh, nhưng sâu bên trong, anh cũng có tấm lòng trung thành và sẵn sàng hy sinh cho bạn bè của mình. Rocket Raccoon được đóng vai bởi Bradley Cooper trong MCU. Anh đã thể hiện một cách xuất sắc tính cách độc đáo và linh hoạt của nhân vật. Rocket là một nhân vật hài hước và thú vị, mang lại sự hòa hợp và sắc thái đặc biệt cho nhóm Guardians of the Galaxy. Rocket Raccoon biểu thị sự mạnh mẽ và lòng kiên nhẫn trong việc vượt qua quá khứ đau khổ và tìm kiếm mục tiêu mới. Anh là một thành viên quan trọng trong đội Quý Ngũ Hùng và đóng góp vào cuộc phiêu lưu bảo vệ vũ trụ khỏi các mối đe dọa.',
    'Groot là một nhân vật siêu anh hùng trong Marvel Cinematic Universe. Anh đã xuất hiện trong các bộ phim như "Guardians of the Galaxy", "Guardians of the Galaxy Vol. 2" và "Avengers: Infinity War". Groot là một chủng cây sống người. Ban đầu, anh là một cái cây và chỉ có khả năng chụp mắt vô cảm và chỉ biết nói "I am Groot." Tuy nhiên, sau khi gặp và làm việc với nhóm Guardians of the Galaxy, Groot đã trở thành một thành viên không thể thiếu và nhận được sự yêu mến của người xem. Không chỉ có vẻ bề ngoài độc đáo, Groot cũng có khả năng kiểm soát cây và sở hữu sức mạnh vật chất vô biên. Anh có thể sử dụng cơ thể mình để tạo ra các vũ khí tự nhiên và có khả năng nảy mình để đánh lại kẻ thù. Dù tưởng chừng như chỉ có tính cách đơn giản, Groot thể hiện sự thông minh và lòng trung thành đến bạn bè. Anh rất quan tâm đến nhóm và thể hiện lòng trung thành, hy sinh vì mục tiêu chung. Groot đã trở thành biểu tượng của tình bạn và lòng đồng đội trong vũ trụ Marvel. Groot được thể hiện bởi việc chia sẻ màn trình diễn giữa diễn viên Vin Diesel và các nhà làm phim sử dụng công nghệ và hiệu ứng đặc biệt để tạo ra nhân vật độc đáo này. Cảm xúc và cái tôi của Groot được truyền đạt qua cách di chuyển và cử chỉ. Groot biểu thị lòng hy sinh và quyết tâm chiến đấu cho nguyên tắc và sự bảo vệ của nhóm. Anh là một nhân vật yêu thích của fan hâm mộ và truyền cảm hứng về sự đoàn kết và tình bạn trong vũ trụ Marvel.']
    i = 0
    for col in [col_1, col_2, col_3, col_4]:
        with col:
            st.image(f'picture/{hinh[i]}', width=150)
            st.markdown(f'<center>{nhan_vat[i]}</center>', unsafe_allow_html=True)
            with st.expander('Tìm hiểu thêm'):
                st.markdown(f'<p style="text-align: justify">{noi_dung[i]}</p>', unsafe_allow_html=True)
        i += 1  

    n = 0
    for col in [col_5, col_6, col_7, col_8]:
        with col:
            st.image(f'picture/{hinh_1[n]}', width=150)
            st.markdown(f'<center>{nhan_vat_1[n]}</center>', unsafe_allow_html=True)
            with st.expander('Tìm hiểu thêm'):
                st.markdown(f'<p style="text-align: justify">{noi_dung_1[n]}</p>', unsafe_allow_html=True)
        n += 1 
    
    i = 0
    for col in [col_9, col_10, col_11, col_12]:
        with col:
            st.image(f'picture/{hinh_2[i]}', width=150)
            st.markdown(f'<center>{nhan_vat_2[i]}</center>', unsafe_allow_html=True)
            with st.expander('Tìm hiểu thêm'):
                st.markdown(f'<p style="text-align: justify">{noi_dung_2[i]}</p>', unsafe_allow_html=True)
        i += 1 

    i = 0
    for col in [col_13, col_14, col_15, col_16]:
        with col:
            st.image(f'picture/{hinh_3[i]}', width=150)
            st.markdown(f'<center>{nhan_vat_3[i]}</center>', unsafe_allow_html=True)
            with st.expander('Tìm hiểu thêm'):
                st.markdown(f'<p style="text-align: justify">{noi_dung_3[i]}</p>', unsafe_allow_html=True)
        i += 1 

    i = 0
    for col in [col_17, col_18, col_19, col_20]:
        with col:
            st.image(f'picture/{hinh_4[i]}', width=150)
            st.markdown(f'<center>{nhan_vat_4[i]}</center>', unsafe_allow_html=True)
            with st.expander('Tìm hiểu thêm'):
                st.markdown(f'<p style="text-align: justify">{noi_dung_4[i]}</p>', unsafe_allow_html=True)
        i += 1 
elif chon == 'Những dự án sắp tới':
    st.markdown(f'<h2><center>{chon}</center></h2>', unsafe_allow_html=True)
    tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(['2021', '2022', '2023', '2024', '2025', '2026', '2027'])
    with tab1:
        col1, col2, col3 = st.columns(3)
        col1.image("picture/Shang_Chi.jpg", width=200)
        col1.markdown('[Shang-Chi and the Legend of the Ten Rings](https://www.marvel.com/movies/shang-chi-and-the-legend-of-the-ten-rings "Bộ phim")')
        col2.image("picture/Eternals.jpg", width=200)
        col2.markdown('[Eternals](https://www.marvel.com/movies/eternals "Bộ phim")')
        col3.image("picture/Spider_Man_3.jpg", width=200)
        col3.markdown('[Spider-Man: No Way Home](https://www.marvel.com/movies/spider-man-no-way-home "Bộ phim")')
    with tab2:
        col1, col2, col3 = st.columns(3)
        col1.image("picture/Doctor_Strange_2.jpg", width=200)
        col1.markdown('[Doctor Strange in the Multiverse of Madness](https://www.marvel.com/movies/doctor-strange-in-the-multiverse-of-madness "Bộ phim")')
        col2.image("picture/Thor_4.jpg", width=200)
        col2.markdown('[Thor: Love and Thunder](https://www.marvel.com/movies/thor-love-and-thunder "Bộ phim")')
        col3.image("picture/Black_Panther_2.jpg", width=200)
        col3.markdown('[Black Panther: Wakanda Forever](https://www.marvel.com/movies/black-panther-wakanda-forever "Bộ phim")')
    with tab3:
        col1, col2, col3 = st.columns(3)
        col1.image("picture/Ant_Man_3.jpg", width=200)
        col1.markdown('[Ant-Man and The Wasp: Quantumania](https://www.marvel.com/movies/ant-man-and-the-wasp-quantumania "Bộ phim")')
        col2.image("picture/Guardians of the Galaxy_2.jpg", width=200)
        col2.markdown('[Guardians of the Galaxy Vol. 3](https://www.marvel.com/movies/guardians-of-the-galaxy-volume-3 "Bộ phim")')
        col3.image("picture/The_Marvels.jpg", width=200)
        col3.markdown('[The Marvels](https://www.marvel.com/movies/the-marvels "Bộ phim")')
    with tab4:
        col1, col2, col3 = st.columns(3)
        col1.image("picture/Deadpool.jpg", width=200)
        col1.markdown('[Deadpool](https://www.marvel.com/movies/deadpool-3 "Bộ phim")')
        col2.image("picture/Captain_America_4.jpg", width=200)
        col2.markdown('[Captain America: Brave New World](https://www.marvel.com/movies/captain-america-brave-new-world "Bộ phim")')
        col3.image("picture/Thunderbolts.jpg", width=200)
        col3.markdown('[Thunderbolts](https://www.marvel.com/movies/thunderbolts "Bộ phim")')
    with tab5:
        col1, col2, col3 = st.columns(3)
        col1.image("picture/Blade.jpg", width=200)
        col1.markdown('[Blade](https://www.marvel.com/movies/blade "Bộ phim")')
        col2.image("picture/F4.jpg", width=200)
        col2.markdown('[Fantastic Four](https://www.marvel.com/movies/fantastic-four "Bộ phim")')
    with tab6:
        col1, col2, col3 = st.columns(3)
        col1.image("picture/Avengers_2026.jpg", width=200)
        col1.markdown('[Avengers: The Kang Dynasty](https://www.marvel.com/movies/avengers-kang-dynasty "Bộ phim")')
    with tab7:
        col1, col2, col3 = st.columns(3)
        col1.image("picture/Avengers_2027.jpg", width=200)
        col1.markdown('[Avengers: Secret Wars](https://www.marvel.com/movies/avengers-secret-wars "Bộ phim")')
elif chon == 'Thống kê':
    st.markdown(f'<h2><center>{chon}</center></h2>', unsafe_allow_html=True)
    nam = pd.DataFrame({'year':["2008", "2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019", "2021"]
                    , 'count': [2, 1, 2, 1, 2, 2, 2, 2, 3, 3, 3, 1]})
    sns.barplot(data = nam, x = 'year', y = 'count')
    plt.title('Thống kê số phim mỗi năm Marvel Studios sản xuất')
    plt.xlabel('Năm')
    plt.ylabel('Số phim')
    st.pyplot()
else:
    st.markdown(f'<h2><center>{chon}</center></h2>', unsafe_allow_html=True)
    phim = mcu['Phim']
    option = st.selectbox('Bạn muốn đánh giá phim nào?', (phim))
    diem_so = st.number_input(f'Số điểm bạn muốn dành cho bộ phim {option}.', 0.1, 10.0, step=0.1)
    nut = st.button('Xin mời đánh giá!')
    if nut:
        if 10 >= diem_so >= 7.0:
            st.write(f'Cảm ơn bạn vì đã đánh giá. Có vẻ như bạn thích bộ phim {option}!')
            st.image('picture/Like.jpg')
        elif 6.9 >= diem_so >= 5:
            st.write(f'Cảm ơn bạn vì đã đánh giá. Chúng tôi sẽ cố gắng cải thiện chất lượng phim!')
            st.image('picture/Neutral.jpg')
        else:
            st.write(f'Cảm ơn bạn vì đã đánh giá. Có vẻ như bạn không thích bộ phim {option}! Chúng tôi sẽ cố gắng cải thiện chất lượng phim!')
            st.image('picture/Dislike.jpg')
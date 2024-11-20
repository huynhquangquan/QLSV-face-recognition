Quá bận để ghi Readme.md =)).

Training model nhận diện đối tượng ở face_recognition_model_face_detecting.

Training model nhận diện giả mạo ở cnn_model_face_detecting

Test model ở face_recognition_face_detecting.

Chạy GUI_Main để mở api.

GUI_Main là nơi chứ mọi code liên quan đến Tinker, connect database (connection, def cuối ở file mananging_function).

CNN và face_recognition cùng thực hiện 1 nv, nhưng CNN được sử dụng với mục đích nhận diện khuôn mặt giả mạo, khuôn mặt thật, face_recognition sẽ đảm nhiệm nhận diện người đó là ai. Nhận diện gian lận qua CNN là 1 phương pháp rẻ tiền, nhưng độ hiệu quả của nó thua rất xa với các camera nhận diện giả mạo khác như camera phân nhiệt.

database là nơi chứa csdl, quên đặt định dạng txt thay vì py =)). Xài xampp và chèn cái này vào SQL.

Các file py còn lại là chức năng hệ thống đi kèm với GUI, nhưng có 1 vài thay vì chạy def, thì chạy bằng OS. Nên sẽ rất khó, đặc biệt là với UNIX-OS like.

Sẽ cập nhật Readme.md sau khi xong năm 3 (nửa năm 2025).

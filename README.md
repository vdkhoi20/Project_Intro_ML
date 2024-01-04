
# Trợ Lí Sức Khỏe Thông Minh

**Group ID: 01**

**Members:**
- **ID 1:** 20127045 - Võ Đình Khôi (33%)
- **ID 2:** 20127411 - Đỗ Đạt Thành (27%)
- **ID 3:** 21127290 - Nguyễn Gia Hưng (23%)
- **ID 4:** 21127005 - Lê Trọng Đức Anh (17%)

## I. Giới thiệu

<![endif]--> Với sự phát triển mạnh mẽ của khoa học ngày nay, với những công nghệ ngày càng tiên tiến sau khoảng thời gian dài tập trung vào những nghiên cứu về mặt kỹ thuật, để các lĩnh vực quan trọng nhằm phục vụ đời sống con người ngày càng phát triển mạnh mẽ. Trong số đó, lĩnh vực liên quan về sức khỏe luôn được quan tâm với hệ thống thăm khám và chữa trị ngày càng phát triển mạnh mẽ, đến những căn bệnh được xem là nan y thời kỳ xưa cũ nay cũng chỉ được xem là những căn bệnh bình thường có thể đặc trị dễ dàng với quy trình thăm khám giữa bệnh nhân – bác sĩ ngày càng chặt chẽ và cũng như chuyên môn của ngành y ngày càng được đảm bảo. Tuy nhiên, sau đại dịch COVID-19, chúng ta đã xác định được tầm quan trọng của mạng internet, cũng như những tác vụ cần thiết để đảm bảo được nhu cầu đời sống của con người thông qua sức mạnh công nghệ này. Việc không thể thực hiện tiếp xúc cơ bản với xã hội đã khiến nhiều vấn đề phát sinh cũng như khiến cho nhiều tác vụ không thể hoạt động bình thường, thậm chí là đáp ứng cho nhu cầu về sức khỏe cũng không thể đảm bảo vì rất khó để có thể tiếp xúc trực tiếp thăm khám như bình thường. Điều đó đã khiến cho độ khó việc phán đoán bệnh và chữa trị nâng cao. Giả sử trường hợp chúng ta đã phát triển hoàn chỉnh hệ thống thăm khám sức khỏe thông qua hệ thống công nghệ hiện đại và có thể truyền đạt qua mạng internet thì dù không thể tiếp xúc trực tiếp cũng không quá khó khăn để có thể điều trị cho bệnh nhân. Để nói một cách chi tiết, rõ ràng hơn thì chúng ta cần có hệ thống tìm kiếm và phân tích thông tin về sức khỏe một cách chính xác, có tập trung và được cập nhật mới thường xuyên hơn bởi vì hiện nay, người bệnh khi muốn tra cứu về những triệu chứng căn bệnh trên những công cụ tìm kiếm mạnh mẽ và phổ biến như Google, Bing, … thì kết quả nhận lại là những căn bệnh với triệu chứng năng hơn rất nhiều so với triệu chứng mà bệnh nhân mắc phải, trong số đó có lẽ kết quả mà bệnh nhân nhận được nhiều nhất là ung thư. Trong khi đó, hiện nay đã có những mô hình học máy ứng dụng vào vấn đề liên quan đến sức khỏe với độ chính xác đang dần được cải thiện ngày càng tốt hơn. Sau khi tìm hiểu nhóm em đã quyết định sử dụng những mô hình được huấn luyện sẵn để tạo thành những chức năng phục vụ cho việc tư vấn và cung cấp thông tin về sức khỏe. Sau khoảng thời gian tìm hiểu, nhóm em đã tạo nên một hệ thống ứng dụng liên quan về sức khỏe tích hợp các chức năng từ những mô hình được huấn luyện sẵn để có thể tư vấn và cung cấp thông tin cho bệnh nhân.

## II. Chức năng trong hệ thống

### Tư vấn sức khỏe

 Chức năng tư vấn sức khỏe được hình thành bằng cách gọi API mô hình GPT-3.5-turbo. Mô hình này sử dụng kiến trúc Transformer để hiểu ngữ cảnh của câu và tạo ra câu trả lời phù hợp. Mô hình này đã được chứng minh là hiệu quả trong việc tạo ra các câu trả lời tự nhiên và chính xác. Đáng chú ý, GPT-3.5-turbo là một phiên bản của mô hình ngôn ngữ GPT-3 được tối ưu hóa về tốc độ. Mô hình này có thể tạo văn bản nhanh hơn tới 10 lần so với mẫu GPT-3.0 ban đầu. Điều này đạt được bằng cách sử dụng một số kỹ thuật, bao gồm: mô hình nhỏ hơn với ít tham số hơn, kiến trúc hiệu quả hơn, và kỹ thuật đào tạo hiệu quả hơn. Với những đặc tính nêu trên, mô hình sẽ mang lại độ chính xác cao trong việc tư vấn sức khỏe cho người dùng với tốc độ trả lời nhanh. Để có thể sử dụng chức năng, người dùng chỉ cần nhập vào những vấn đề thắc mắc về sức khỏe, ứng dụng sẽ hình thành nên câu trả lời tư vấn cho người dùng dựa trên những thông tin hiện có.
 

### Sinh ra ảnh triệu chứng bệnh (ngoài da)

Hoạt động dựa trên mô hình SD-XL 1.0 huấn luyện sẵn được cung cấp sử dụng trên Hugging Face và được phát triển bởi Stability AI. Mô hình này sử dụng một kiến trúc UNet lớn hơn và một bối cảnh cross-attention lớn hơn nhờ sử dụng một bộ mã hóa văn bản thứ hai. SDXL 1.0 tạo ra hình ảnh chất lượng cao trong hầu hết các phong cách nghệ thuật và là mô hình mở tốt nhất cho việc tạo hình ảnh thực. Hình ảnh rõ ràng có thể được tạo ra mà không cần có bất kỳ ‘cảm giác’ nào được truyền đạt bởi mô hình, đảm bảo tự do tuyệt đối về phong cách. Mô hình này đã được chứng minh là hiệu quả trong việc tạo ra các hình ảnh chất lượng cao từ các dấu hiệu văn bản. Chức năng chính của mô hình này là tạo ra hình ảnh minh họa theo từ ngữ diễn tả của người dùng. Lý do cho mô hình này được chọn là bởi vì độ chính xác cao đã được kiểm nghiệm và so sánh với các mô hình tương tự trước đó. Tuy vẫn chưa đạt được độ chính xác tối ưu nhất nhưng mô hình vẫn mang lại chức năng cần thiết cho người dùng, giúp người dùng hình dung rõ nét hơn về triệu chứng căn bệnh ngoài da mà bản thân đang gặp phải. Để sử dụng chức năng, người dùng sẽ nhập vào miêu tả về căn bệnh ngoài da, hệ thống sẽ sinh ra hình ảnh tương ứng với căn bệnh đó dựa trên tập dữ liệu được huấn luyện sẵn trước đó.

### Nhận biết ảnh triệu chứng bệnh (ngoài da)

Hoạt động bằng cách gọi Detect Skin Disease API được cung cấp từ AILabTools. Detect Skin Disease API nhận hình ảnh tự nhiên của da và dự đoán phân loại các bệnh da1. API này có thể phát hiện 24 bệnh da phổ biến. API này hoạt động dựa trên các thuật toán học máy để phân loại các hình ảnh da và đưa ra dự đoán về loại bệnh da. API này đã được chứng minh là chính xác và hiệu quả. Để sử dụng được chức năng, người dùng cần cung cấp hình ảnh tình trạng da hiện tại dưới định dạng JPG, PNG, kích thước không vượt quá 20MB và độ phân giải phải thấp hơn 1280x1280px. Sau khi đã cung cấp hình ảnh, hệ thống sẽ đưa ra kết quả dự đoán bộ phận cơ thể trong ảnh và xác suất phần trăm nguy cơ mắc bệnh.

### d. Nhận biết ảnh X-Quang phổi

Hoạt động dựa trên mô hình YOLOv8 Chest Xray Classification được phát triển bởi Mô hình YOLOv8 Chest Xray Classification được phát triển bởi keremberke và được đăng tải trên Hugging Face. YOLOv8 là một mô hình phát hiện đối tượng nhanh, chính xác và dễ sử dụng, được phát triển bởi Ultralytics. YOLOv8 xây dựng trên thành công của các phiên bản YOLO trước đó và giới thiệu các tính năng và cải tiến mới để tăng cường hiệu suất và linh hoạt. Mô hình YOLOv8 được sử dụng trong hệ thống là một mô hình được tinh chỉnh (finetuned) cho nhiệm vụ phân loại ảnh X-quang ngực. Mô hình này có thể phân biệt được hai nhãn: NORMAL (bình thường) và PNEUMONIA (viêm phổi). Mô hình này có độ chính xác top-1 là 0.955 và top-5 là 1.000, cao hơn các mô hình YOLOv8 khác như YOLOv8n và YOLOv8s. Mô hình này cũng có thể phát hiện các đối tượng khác với độ chính xác cao. Cách thức sử dụng chức năng cũng rất đơn giản, chỉ cần người dung cung cấp hình ảnh X-Quang ngực, hệ thống sẽ đưa ra kết quả dự đoán xác suất phần trăm bị ung thư hoặc không dựa trên hình ảnh được cung cấp.

## III. Các kiến trúc và tính năng nổi bật của các pretrained model được sử dụng

### a. ChatGPT

- **Kiến trúc:** GPT (Transformer)
- **Tính năng:** ChatGPT xây dựng trên kiến trúc GPT, một mô hình Transformer pre-trained. Transformer là một kiến trúc mạng nơ-ron chủ yếu dựa trên cơ chế tự chú ý (self-attention), giúp mô hình hiểu được các mối quan hệ không gian và ngữ nghĩa trong dữ liệu văn bản. Mô hình GPT được huấn luyện trước trên một lượng lớn dữ liệu văn bản không gán nhãn từ Internet.

- The fine-tuning process leveraged both [supervised learning](https://en.wikipedia.org/wiki/Supervised_learning "Supervised learning") as well as [reinforcement learning](https://en.wikipedia.org/wiki/Reinforcement_learning "Reinforcement learning") in a process called [reinforcement learning from human feedback](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback "Reinforcement learning from human feedback") (RLHF). These rankings were used to create "reward models" that were used to fine-tune the model further by using several iterations of [Proximal Policy Optimization](https://en.wikipedia.org/wiki/Proximal_Policy_Optimization "Proximal Policy Optimization") (PPO)

### b. YOLO

- **Kiến trúc:** CNN (Convolutional Neural Network)
- **Tính năng:** YOLO sử dụng một mạng nơ-ron dựa trên kiến trúc CNN (Convolutional Neural Network).Ảnh được chia thành lưới ô và mỗi ô dự đoán nhiều bounding boxes cùng lúc. Mỗi bounding box chứa thông tin về vị trí và xác suất của các lớp đối tượng. YOLO chạy nhanh vì chỉ yêu cầu một lần chạy qua toàn bộ ảnh để thực hiện các dự đoán.


### c. Stable Diffusion

- **Kiến trúc:** Denoising Diffusion Probabilistic Models
- **Tính năng:** Là một Denoising Diffusion Probabilistic Models dựa vào cơ chế cross attention để conditioning nhiều task vụ như là text-image, image->image,..

## IV. Khó khăn gặp phải và cách giải quyết

### a. Khó khăn

- Lần đầu tiên tiếp xúc với mô hình học máy
- Mô hình được huấn luyện dựa trên bộ dữ liệu chung không tập trung vào vấn đề sức khỏe
- Nhiều mô hình để lựa chọn Tìm hiểu và so sánh để chọn mô hình tốt nhất.
- Mất gói tin khi gọi API ChatGPT .
- GPU COLAB không đủ RAM  để deploy nhiều model cùng lúc .

### b. Cách giải quyết

- **Học hỏi và đọc tài liệu:** Nắm vững kiến thức về mô hình học máy.
- **So sánh kết quả:** Chọn mô hình tốt nhất cho vấn đề cụ thể, chạy thử test nhiều để xem model có tốt với vấn đề mình cần giải quyết.
- **Tìm hiểu và so sánh mô hình:** Lựa chọn mô hình phù hợp nhất.
- **Giới hạn số tokens trả về cho API ChatGPT:** Đảm bảo truy vấn hiệu quả.
- **Gọi API thay thế cho mô hình**.

## V. Kết luận

Vậy nên nhóm em tin rằng ứng dụng tư vấn sức khỏe này sẽ có thể mang lại nhiều lợi ích cho người dùng với các chức năng đã liệt kê. Không chỉ vậy ứng dụng này có tiềm năng để trở thành một công cụ mạnh mẽ hỗ trợ người dùng có thể hiểu rõ hơn về sức khỏe của mình. Tuy nhiên, cần lưu ý rằng ứng dụng này không thể thay thế cho việc thăm khám y tế chuyên nghiệp mà chỉ là hỗ trợ và giúp người dùng có được thông tin liên quan một cách tập trung và chính xác nhất có thể.

## VI. Nguồn tham khảo

- [Models - OpenAI API](https://platform.openai.com/docs/models/gpt-3-5)
-  [What Is GPT-3.5 Turbo? - PC Guide](https://www.pcguide.com/apps/gpt-3-5-turbo/)
- [stabilityai/stable-diffusion-xl-base-1.0 · Hugging Face](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0)
- [Announcing SDXL 1.0 — Stability AI](https://stability.ai/news/stable-diffusion-sdxl-1-announcement)
- [Detect Skin Disease API | AILabTools](https://www.ailabtools.com/doc/ai-portrait/analysis/skin-disease-detection/api)
- [keremberke/yolov8n-chest-xray-classification · Hugging Face](https://huggingface.co/keremberke/yolov8n-chest-xray-classification)
- [awesome yolov8 models](https://yolov8.xyz/#/)

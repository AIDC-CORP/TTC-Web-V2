
import { Project, Article, Service } from '../types';

export const projects: Project[] = [
  {
    id: 'du-an-vinhome-grand-park',
    name: 'Vinhomes Grand Park',
    image: 'https://picsum.photos/seed/project1/800/600',
    summary: 'Khu đô thị thông minh đẳng cấp quốc tế tại TP. Hồ Chí Minh.',
    description: 'Dự án Vinhomes Grand Park là một đại đô thị thông minh được quy hoạch theo mô hình compound khép kín, mang đến một môi trường sống lý tưởng với đầy đủ tiện ích và không gian xanh. Chúng tôi tự hào đã tham gia vào hạng mục tư vấn thiết kế cảnh quan cho dự án này.',
    investor: 'Tập đoàn Vingroup',
    executionTime: '2019 - 2022',
    gallery: [
      'https://picsum.photos/seed/gallery1a/1200/800',
      'https://picsum.photos/seed/gallery1b/1200/800',
      'https://picsum.photos/seed/gallery1c/1200/800',
      'https://picsum.photos/seed/gallery1d/1200/800',
    ],
    category: 'Đô thị'
  },
  {
    id: 'du-an-sun-world-ba-na-hills',
    name: 'Sun World Ba Na Hills',
    image: 'https://picsum.photos/seed/project2/800/600',
    summary: 'Tổ hợp du lịch nghỉ dưỡng và giải trí hàng đầu Việt Nam.',
    description: 'Tân Thành Công đã cung cấp giải pháp tư vấn kết cấu cho một số hạng mục quan trọng tại Sun World Ba Na Hills, đảm bảo tính an toàn và thẩm mỹ cho công trình trong điều kiện địa hình phức tạp.',
    investor: 'Tập đoàn Sun Group',
    executionTime: '2018 - 2020',
    gallery: [
      'https://picsum.photos/seed/gallery2a/1200/800',
      'https://picsum.photos/seed/gallery2b/1200/800',
    ],
    category: 'Du lịch'
  },
  {
    id: 'du-an-e-factory-tan-thuan',
    name: 'Nhà máy E-Factory Tân Thuận',
    image: 'https://picsum.photos/seed/project3/800/600',
    summary: 'Nhà máy sản xuất linh kiện điện tử hiện đại tại khu chế xuất.',
    description: 'Đây là dự án tiêu biểu trong lĩnh vực xây dựng công nghiệp của chúng tôi. Dự án bao gồm thiết kế và thi công toàn bộ nhà xưởng, văn phòng và các công trình phụ trợ, đáp ứng tiêu chuẩn quốc tế.',
    investor: 'Công ty TNHH Điện tử ABC',
    executionTime: '2021',
    gallery: [
      'https://picsum.photos/seed/gallery3a/1200/800',
      'https://picsum.photos/seed/gallery3b/1200/800',
      'https://picsum.photos/seed/gallery3c/1200/800',
    ],
    category: 'Công nghiệp'
  },
   {
    id: 'du-an-cau-thu-thiem-2',
    name: 'Cầu Thủ Thiêm 2',
    image: 'https://picsum.photos/seed/project4/800/600',
    summary: 'Biểu tượng kiến trúc mới kết nối trung tâm TP. Hồ Chí Minh.',
    description: 'Chúng tôi đã tham gia vào quá trình giám sát thi công và tư vấn giải pháp vật liệu cho dự án Cầu Thủ Thiêm 2, một công trình có yêu cầu kỹ thuật và mỹ thuật cao.',
    investor: 'UBND TP. Hồ Chí Minh',
    executionTime: '2015 - 2022',
    gallery: [
      'https://picsum.photos/seed/gallery4a/1200/800',
      'https://picsum.photos/seed/gallery4b/1200/800',
    ],
    category: 'Hạ tầng'
  },
];

export const articles: Article[] = [
  {
    id: 'xu-huong-vat-lieu-xay-dung-ben-vung',
    title: 'Xu Hướng Vật Liệu Xây Dựng Bền Vững Năm 2024',
    image: 'https://picsum.photos/seed/blog1/800/450',
    excerpt: 'Khám phá các loại vật liệu xây dựng thân thiện với môi trường đang trở thành xu hướng và định hình tương lai của ngành kiến trúc.',
    content: 'Ngành xây dựng đang chứng kiến một cuộc cách mạng xanh, với sự trỗi dậy mạnh mẽ của các vật liệu bền vững. Từ bê tông tái chế, gỗ kỹ thuật cho đến các vật liệu cách nhiệt từ sợi tự nhiên, việc lựa chọn vật liệu không chỉ còn dựa trên chi phí và độ bền mà còn cả tác động đến môi trường. Bài viết này sẽ đi sâu vào các loại vật liệu tiềm năng và ứng dụng của chúng trong các công trình hiện đại, góp phần tạo nên những không gian sống xanh và an toàn hơn.',
    publishDate: '2024-05-15',
    category: 'Blog'
  },
  {
    id: 'bim-va-cuoc-cach-mang-so-hoa',
    title: 'BIM và Cuộc Cách Mạng Số Hóa trong Ngành Xây Dựng',
    image: 'https://picsum.photos/seed/blog2/800/450',
    excerpt: 'Mô hình thông tin công trình (BIM) đang thay đổi hoàn toàn cách chúng ta thiết kế, thi công và quản lý dự án. Tìm hiểu lợi ích của BIM.',
    content: 'Mô hình thông tin công trình (BIM) không còn là một khái niệm xa lạ. Nó đã và đang trở thành công cụ không thể thiếu, giúp tối ưu hóa quy trình làm việc, giảm thiểu sai sót và tiết kiệm chi phí đáng kể. Từ giai đoạn lên ý tưởng thiết kế, phân tích kết cấu, dự toán chi phí cho đến quản lý vận hành sau khi hoàn công, BIM mang lại một cái nhìn toàn diện và chính xác, kết nối tất cả các bên liên quan trên một nền tảng duy nhất.',
    publishDate: '2024-04-22',
    category: 'Blog'
  },
  {
    id: 'tu-van-giam-sat-thi-cong-chuyen-nghiep',
    title: 'Tầm Quan Trọng Của Tư Vấn Giám Sát Thi Công Chuyên Nghiệp',
    image: 'https://picsum.photos/seed/service1/800/450',
    excerpt: 'Một đội ngũ tư vấn giám sát giỏi sẽ là chìa khóa đảm bảo chất lượng, tiến độ và sự an toàn cho mọi công trình.',
    content: 'Vai trò của tư vấn giám sát không chỉ dừng lại ở việc kiểm tra bản vẽ và theo dõi tiến độ. Một đơn vị giám sát chuyên nghiệp sẽ chủ động phát hiện các rủi ro tiềm ẩn, đề xuất các giải pháp kỹ thuật tối ưu, quản lý chất lượng vật liệu đầu vào và đảm bảo công trình được thi công đúng theo thiết kế và tiêu chuẩn kỹ thuật. Đầu tư vào dịch vụ tư vấn giám sát là một khoản đầu tư thông minh để bảo vệ giá trị công trình của bạn.',
    publishDate: '2024-03-10',
    category: 'Tư vấn'
  },
    {
    id: 'giai-phap-phong-chay-chua-chay-hieu-qua',
    title: 'Giải Pháp Tối Ưu Cho Hệ Thống Phòng Cháy Chữa Cháy',
    image: 'https://picsum.photos/seed/service2/800/450',
    excerpt: 'An toàn phòng cháy chữa cháy là yếu tố tiên quyết trong mọi công trình. Chúng tôi cung cấp dịch vụ tư vấn thiết kế và thẩm duyệt PCCC.',
    content: 'Với các quy định ngày càng chặt chẽ về an toàn PCCC, việc thiết kế một hệ thống hiệu quả và tuân thủ pháp luật là vô cùng quan trọng. Dịch vụ của chúng tôi bao gồm khảo sát, lên phương án thiết kế, lựa chọn thiết bị phù hợp và hỗ trợ chủ đầu tư trong quá trình thẩm duyệt với cơ quan chức năng, đảm bảo hệ thống PCCC của bạn không chỉ an toàn mà còn tối ưu về chi phí.',
    publishDate: '2024-02-18',
    category: 'Tư vấn'
  },
];

export const services: Service[] = [
  {
    id: 'tu-van-thiet-ke',
    name: 'Tư vấn thiết kế',
    image: 'https://picsum.photos/seed/service_icon1/400/300',
    summary: 'Cung cấp giải pháp thiết kế kiến trúc, kết cấu và MEP toàn diện.'
  },
  {
    id: 'quan-ly-du-an',
    name: 'Quản lý dự án',
    image: 'https://picsum.photos/seed/service_icon2/400/300',
    summary: 'Đảm bảo dự án hoàn thành đúng tiến độ, chất lượng và ngân sách.'
  },
  {
    id: 'tu-van-giam-sat',
    name: 'Tư vấn giám sát',
    image: 'https://picsum.photos/seed/service_icon3/400/300',
    summary: 'Kiểm soát chất lượng thi công, vật liệu và an toàn lao động.'
  },
  {
    id: 'tham-dinh-du-an',
    name: 'Thẩm định dự án',
    image: 'https://picsum.photos/seed/service_icon4/400/300',
    summary: 'Đánh giá tính khả thi và hiệu quả của các dự án đầu tư xây dựng.'
  }
];

export const allContent: (Project | Article)[] = [...projects, ...articles];

import React from 'react';

const Value: React.FC = () => {
  const values = [
    {
      id: 1,
      label: 'CÔNG NGHỆ',
      title: 'CÔNG NGHỆ',
      description: 'Áp dụng công nghệ tiên tiến sử dụng nhà thép tiền chế trong việc xây dựng nhà máy cho các doanh nghiệp.',
    },
    {
      id: 2,
      label: 'TẦM NHÌN',
      title: 'TẦM NHÌN',
      description: 'Đội ngũ kỹ sư với nhiều năm kinh nghiệm trong việc tư vấn & thiết kế sẽ giúp bạn hiện thực hóa nhà máy tiêu chuẩn quốc tế.',
    },
    {
      id: 3,
      label: 'THIẾT BỊ',
      title: 'THIẾT BỊ',
      description: 'Trang thiết bị máy móc và công nghệ hiện đại được vận hành bởi đội ngũ công nhân với tay nghề bậc 7/7',
    },
    {
      id: 4,
      label: 'ĐỊNH HƯỚNG',
      title: 'ĐỊNH HƯỚNG',
      description: 'Sự hài lòng của Quý khách hàng chính là mục tiêu và động lực lớn nhất để Tân Thành Công luôn luôn hướng đến.',
    },
  ];

  return (
    <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
      {values.map((value) => (
        <div
          key={value.id}
          className="relative bg-gradient-to-br from-blue-500 to-blue-600 rounded-3xl p-8 md:p-10 shadow-xl overflow-hidden group hover:shadow-2xl transition-shadow duration-300"
        >
          {/* Decorative corner circle */}
          <div className="absolute -top-16 -right-16 w-40 h-40 bg-blue-400 rounded-full opacity-20 group-hover:opacity-30 transition-opacity"></div>

          {/* Quote mark icon */}
          <div className="text-5xl md:text-6xl text-white opacity-30 mb-4">‟</div>

          {/* Label badge */}
          <div className="inline-block mb-4 px-3 py-1 bg-white rounded-full">
            <span className="text-sm font-semibold text-blue-600">{value.label}</span>
          </div>

          {/* Content */}
          <h3 className="text-2xl md:text-3xl font-bold text-white mb-3 leading-tight relative z-10">
            {value.title}
          </h3>
          <p className="text-white text-base md:text-lg leading-relaxed relative z-10">
            {value.description}
          </p>

          {/* Closing quote mark */}
          <div className="absolute bottom-4 right-6 text-5xl md:text-6xl text-white opacity-20">‟</div>
        </div>
      ))}
    </div>
  );
};

export default Value;

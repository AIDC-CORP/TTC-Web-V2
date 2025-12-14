
import React, { useState } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { FaPlus, FaTimes, FaCheckCircle } from 'react-icons/fa';

interface Hotspot {
    id: string;
    label: string;
    x: number; // percentage from left
    y: number; // percentage from top
    title: string;
    description: string;
    details: string[];
}

const hotspots: Hotspot[] = [
    {
        id: 'foundation',
        label: '01',
        x: 10,
        y: 90,
        title: 'Móng Bê Tông Cốt Thép',
        description: 'Hệ thống móng vững chắc, đảm bảo khả năng chịu tải trọng lớn cho toàn bộ công trình.',
        details: [
            'Bulong neo cường độ cao (Grade 5.6, 8.8)',
            'Bê tông mác 250-300 tùy tải trọng',
            'Thi công chính xác theo bản vẽ định vị'
        ]
    },
    {
        id: 'column',
        label: '02',
        x: 23,
        y: 55,
        title: 'Khung Thép Tiền Chế (Cột & Kèo)',
        description: 'Hệ khung thép tổ hợp chữ I biến thiên tiết diện, tối ưu hóa khả năng chịu lực và tiết kiệm vật liệu.',
        details: [
            'Thép tấm cường độ cao (Q345B)',
            'Sơn chống rỉ Alkyd hoặc Epoxy 2 lớp',
            'Liên kết bu lông cường độ cao'
        ]
    },
    {
        id: 'roof',
        label: '03',
        x: 50,
        y: 15,
        title: 'Hệ Mái Seamlock/Cliplock',
        description: 'Hệ thống mái tôn không bắn vít, chống dột tuyệt đối và chịu được bão lớn.',
        details: [
            'Tôn mạ kẽm/mạ màu dày 0.45mm - 0.5mm',
            'Lớp cách nhiệt túi khí hoặc bông thủy tinh (Glasswool)',
            'Độ dốc mái tiêu chuẩn 10-15%'
        ]
    },
    {
        id: 'ventilation',
        label: '04',
        x: 65,
        y: 5, // Top center-ish, adjusted for diagram
        title: 'Hệ Thống Thông Gió Đỉnh Mái',
        description: 'Giải pháp luân chuyển không khí tự nhiên, giảm nhiệt độ bên trong nhà xưởng hiệu quả.',
        details: [
            'Cửa trời (Monitor) đón gió',
            'Quả cầu thông gió inox',
            'Tấm lợp lấy sáng Polycarbonate'
        ]
    },
    {
        id: 'wall',
        label: '05',
        x: 85,
        y: 60,
        title: 'Thưng Tường & Vách Bao Che',
        description: 'Hệ vách tôn hoặc tường gạch đảm bảo an ninh và thẩm mỹ cho công trình.',
        details: [
            'Xây tường gạch 110/220 cao 2m-3m chân tường',
            'Tôn vách mạ màu dày 0.4mm',
            'Hệ giằng vách tăng độ cứng'
        ]
    }
];

export const FactoryAnatomySection = () => {
    const [activeSpot, setActiveSpot] = useState<Hotspot>(hotspots[1]); // Default to column

    return (
        <section className="py-20 bg-gray-50 overflow-hidden">
            <div className="container mx-auto px-4">
                <div className="text-center mb-16">
                    <motion.h2
                        initial={{ opacity: 0, y: 20 }}
                        whileInView={{ opacity: 1, y: 0 }}
                        viewport={{ once: true }}
                        className="text-3xl md:text-4xl font-bold text-gray-900 mb-4"
                    >
                        Giải Phẫu Kỹ Thuật <span className="text-[#0057B7]">Nhà Xưởng</span>
                    </motion.h2>
                    <p className="text-gray-600 max-w-2xl mx-auto">
                        Khám phá chi tiết cấu tạo bên trong một công trình nhà thép tiền chế tiêu chuẩn do Tân Thành Công thực hiện.
                    </p>
                </div>

                <div className="flex flex-col lg:flex-row gap-8 items-center justify-center">
                    {/* Interactive Diagram Area */}
                    <div className="relative w-full lg:w-2/3 max-w-4xl aspect-[16/9] bg-white rounded-xl shadow-lg border border-gray-200 overflow-hidden">
                        {/* You can replace this src with your actual blueprint image */}
                        <img
                            src="/factory-anatomy.png"
                            alt="Factory Anatomy Diagram"
                            className="w-full h-full object-contain p-4"
                        />

                        {/* Hotspots Layer */}
                        <div className="absolute inset-0 top-10">
                            {hotspots.map((spot) => (
                                <button
                                    key={spot.id}
                                    onClick={() => setActiveSpot(spot)}
                                    className={`absolute group focus:outline-none transform -translate-x-1/2 -translate-y-1/2 w-8 h-8 flex items-center justify-center rounded-full transition-all duration-300 z-10
                    ${activeSpot?.id === spot.id
                                            ? 'bg-[#0057B7] text-white scale-125 shadow-[0_0_0_8px_rgba(0,87,183,0.2)]'
                                            : 'bg-white text-gray-800 shadow-md hover:bg-[#0057B7] hover:text-white'
                                        }`}
                                    style={{ left: `${spot.x}%`, top: `${spot.y}%` }}
                                >
                                    <span className="text-xs font-bold">{spot.label}</span>

                                    {/* Pulse Effect for inactive but hoverable */}
                                    {activeSpot?.id !== spot.id && (
                                        <span className="absolute w-full h-full rounded-full bg-[#0057B7] opacity-20 animate-ping"></span>
                                    )}

                                    {/* Tooltip for quick hover info (optional, desktop only) */}
                                    <div className="absolute bottom-full left-1/2 transform -translate-x-1/2 mb-2 w-max px-3 py-1 bg-gray-900 text-white text-xs rounded opacity-0 group-hover:opacity-100 transition-opacity pointer-events-none whitespace-nowrap hidden md:block">
                                        {spot.title}
                                    </div>
                                </button>
                            ))}
                        </div>
                    </div>

                    {/* Info Panel */}
                    <div className="w-full lg:w-1/3 min-h-[400px]">
                        <AnimatePresence mode="wait">
                            {activeSpot && (
                                <motion.div
                                    key={activeSpot.id}
                                    initial={{ opacity: 0, x: 20 }}
                                    animate={{ opacity: 1, x: 0 }}
                                    exit={{ opacity: 0, x: -20 }}
                                    transition={{ duration: 0.3 }}
                                    className="bg-white p-6 rounded-xl shadow-xl border-l-4 border-[#0057B7] h-full"
                                >
                                    <div className="flex items-center gap-4 mb-4">
                                        <div className="w-12 h-12 rounded-full bg-blue-50 flex items-center justify-center text-[#0057B7] font-bold text-xl">
                                            {activeSpot.label}
                                        </div>
                                        <h3 className="text-xl font-bold text-gray-900">{activeSpot.title}</h3>
                                    </div>

                                    <p className="text-gray-600 mb-6 leading-relaxed">
                                        {activeSpot.description}
                                    </p>

                                    <div className="space-y-3">
                                        <h4 className="font-semibold text-gray-800 border-b pb-2 mb-3">Thông số kỹ thuật nổi bật:</h4>
                                        {activeSpot.details.map((detail, index) => (
                                            <motion.div
                                                key={index}
                                                initial={{ opacity: 0, y: 10 }}
                                                animate={{ opacity: 1, y: 0 }}
                                                transition={{ delay: index * 0.1 }}
                                                className="flex items-start gap-3"
                                            >
                                                <span className="text-green-500 mt-1 flex-shrink-0"><FaCheckCircle /></span>
                                                <span className="text-sm text-gray-700">{detail}</span>
                                            </motion.div>
                                        ))}
                                    </div>

                                    <div className="mt-8 pt-6 border-t border-gray-100">
                                        <button className="text-[#0057B7] font-semibold hover:text-blue-700 text-sm flex items-center gap-2 transition-colors">
                                            Xem chi tiết kỹ thuật <span aria-hidden="true">&rarr;</span>
                                        </button>
                                    </div>
                                </motion.div>
                            )}
                        </AnimatePresence>
                    </div>
                </div>
            </div>
        </section>
    );
};

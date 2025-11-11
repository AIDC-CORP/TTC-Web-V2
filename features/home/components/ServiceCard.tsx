
import React from 'react';
import { Service } from '../../../types';

interface ServiceCardProps {
  service: Service;
}

const ServiceCard: React.FC<ServiceCardProps> = ({ service }) => {
  return (
    <div className="bg-white p-8 rounded-lg shadow-md text-center transform hover:scale-105 transition-transform duration-300">
        <img src={service.image} alt={service.name} className="w-24 h-24 mx-auto mb-4 object-cover rounded-full"/>
      <h3 className="text-xl font-bold text-gray-800 mb-2">{service.name}</h3>
      <p className="text-gray-600">{service.summary}</p>
    </div>
  );
};

export default ServiceCard;

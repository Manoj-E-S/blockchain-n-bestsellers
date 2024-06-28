import React from "react";
import { Swiper, SwiperSlide } from "swiper/react";
import { Pagination, Navigation } from "swiper/modules";
import testimonials, { Testimonial } from "../../constants/testimonials";
import "swiper/css";
import "swiper/css/pagination";
import "swiper/css/navigation";

const Testimonials: React.FC = () => {
  return (
    <section className="bg-darkBrown py-10 mb-20">
      <div className="container mx-auto">
        <h2 className="text-4xl font-gallient tracking-wide font-bold text-center mb-6 text-white">What Our Users Say</h2>
        <div className="px-4 sm:px-8 lg:px-16">
          <Swiper
            pagination={{ clickable: true }}
            navigation
            modules={[Pagination, Navigation]}
            className="mySwiper"
          >
            {testimonials.map((testimonial: Testimonial, index: number) => (
              <SwiperSlide key={index}>
                <div className="bg-[#1a1a25] text-white text-xl h-[20vw] p-6 rounded-lg font-raleway flex flex-col items-center justify-center">
                  <p className="mb-4">"{testimonial.feedback}"</p>
                  <p className="font-semibold text-right">- {testimonial.name}</p>
                </div>
              </SwiperSlide>
            ))}
          </Swiper>
        </div>
      </div>
    </section>
  );
};

export default Testimonials;

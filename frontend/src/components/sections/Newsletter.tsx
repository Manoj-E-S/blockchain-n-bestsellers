import React from "react";

const Newsletter: React.FC = () => {
  return (
    <div className="w-full h-[100vh] flex items-center justify-center pb-20">
      <div className="left h-full w-[60%] flex flex-col justify-center p-20">
        <h2 className="text-7xl font-gallient font-bold">Subscribe to our</h2>
        <h2 className="text-5xl font-gallient">Newsletter</h2>
        <div className="relative mt-5 w-96">
          <input
            className="w-full h-12 font-raleway p-2 pl-4 pr-10 border-2 border-gray-500"
            type="text"
            placeholder="Your Email"
          />
          <span className="absolute inset-y-0 right-0 flex items-center pr-3 cursor-pointer">
            <p className="text-3xl font-bold">→</p>
          </span>
        </div>
        <div className="message text-sm font-raleway mt-3">
          <p>By signing up you agree with our <span className="underline">terms and conditions</span>, and <span className="underline">privacy policy</span>.</p>
          <p>To opt out, click unsubscribe from the email.</p>
        </div>
      </div>
      <div className="right h-full w-[40%] bg-green-300 bg-library bg-center bg-cover"></div>
    </div>
  );
};

export default Newsletter;

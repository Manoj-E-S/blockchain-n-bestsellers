import React from "react";
import { useForm } from "react-hook-form";
import { yupResolver } from "@hookform/resolvers/yup";
import * as yup from "yup";
import { NavLink } from "react-router-dom";
import login from "../functions/login";

// Validation schema
const schema = yup.object().shape({
  email: yup
    .string()
    .email("Invalid email address")
    .required("Email is required"),
  password: yup
    .string()
    .min(6, "Password must be at least 6 characters")
    .required("Password is required"),
});

const Login: React.FC = () => {
  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm({
    resolver: yupResolver(schema),
  });

  const onSubmit = async(data: any) => {
    const result = await login(data.email, data.password);
    if(result.ok) {
      // Redirect to dashboard
      console.log("Login successful");
      console.log(result.data);
    }
    else {
      // Display error message
      console.log("Login failed");
      console.log(result.data);
    }
  };

  return (
    <div className="min-h-screen flex font-raleway flex-col md:flex-row">
      <div className="md:w-1/2 bg-stack bg-cover bg-center relative flex items-center justify-center md:justify-start">
        <div className="text-center md:text-left px-4">
          <h1 className="text-4xl md:text-7xl font-bold font-greatVibes text-darkBrown absolute top-[25%] left-[7%]">
            Bookworms and Bestsellers
          </h1>
          <h2 className="text-xl md:text-2xl font-bold font-cormorant text-darkBrown mt-4 md:mt-10 absolute top-[30%] left-[25%]">
            Cultivating a Passion for Reading
          </h2>
        </div>
      </div>
      <div className="flex justify-end w-full md:w-1/2">
        <div className="bg-white min-h-screen w-full flex justify-center items-center p-4">
          <div className="max-w-md w-full">
            <form onSubmit={handleSubmit(onSubmit)}>
              <div>
                <span className="text-sm text-gray-900">Welcome Back</span>
                <h1 className="text-2xl md:text-3xl font-bold">
                  Login to your Account
                </h1>
              </div>
              <div className="mt-5">
                <label className="block text-md mb-2" htmlFor="email">
                  Email
                </label>
                <input
                  className="px-4 w-full border-2 py-2 rounded-md text-sm outline-none"
                  type="email"
                  {...register("email")}
                  placeholder="Email"
                />
                {errors.email && (
                  <p className="text-red-500 text-sm mt-1">
                    {errors.email.message}
                  </p>
                )}
              </div>
              <div className="my-3">
                <label className="block text-md mb-2" htmlFor="password">
                  Password
                </label>
                <input
                  className="px-4 w-full border-2 py-2 rounded-md text-sm outline-none"
                  type="password"
                  {...register("password")}
                  placeholder="Password"
                />
                {errors.password && (
                  <p className="text-red-500 text-sm mt-1">
                    {errors.password.message}
                  </p>
                )}
              </div>
              <div className="flex justify-between items-center">
                <div>
                  <input
                    className="cursor-pointer"
                    type="checkbox"
                    name="rememberme"
                  />
                  <span className="text-sm ml-2">Remember Me</span>
                </div>
                <span className="text-sm text-blue-700 hover:underline cursor-pointer">
                  Forgot password?
                </span>
              </div>
              <div className="mt-4 mb-3 w-full">
                <button
                  className="w-full bg-bronze hover:bg-[#a42727] text-white py-2 rounded-md transition duration-100"
                  type="submit"
                >
                  Login now
                </button>
                <div className="flex space-x-2 justify-center items-center bg-brown hover:bg-[#4b0202] text-white py-2 rounded-md transition duration-100 mt-3">
                  <img
                    className="h-5 cursor-pointer"
                    src="https://i.imgur.com/arC60SB.png"
                    alt="Google"
                  />
                  <button type="button" onClick={() => document.location.href="http://localhost:3000/auth/googlelogin"}>Login with Google</button>
                </div>
              </div>
            </form>
            <p className="mt-8 text-center md:text-left">
              Don't have an account?{" "}
              <NavLink
                to={"/signup"}
                className="cursor-pointer text-sm text-blue-600"
              >
                Sign Up Now!
              </NavLink>
            </p>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Login;

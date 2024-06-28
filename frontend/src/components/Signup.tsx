import React, { useState } from "react";
import { useForm, SubmitHandler } from "react-hook-form";
import { yupResolver } from "@hookform/resolvers/yup";
import * as yup from "yup";
import { motion } from "framer-motion";

interface StepOneInputs {
  name: string;
  email: string;
  password: string;
}

interface StepTwoInputs {
  location: string;
  contact: string;
}

const stepOneSchema = yup.object().shape({
  name: yup.string().required("Name is required"),
  email: yup
    .string()
    .email("Invalid email address")
    .required("Email is required"),
  password: yup
    .string()
    .min(6, "Password must be at least 6 characters")
    .required("Password is required"),
});

const stepTwoSchema = yup.object().shape({
  location: yup.string().required("Location is required"),
  contact: yup.string().required("Contact number is required"),
});

const genres = [
  'Biography', 'History', 'Crime', 'Adventure', 'Thriller', 'Mystery', 'Humor', 
  'Fiction', 'Paranormal', 'Fantasy', 'Romance', 'Adult', 'Children', 'Poetry', 
  'Comic', 'Horror', 'Nonfiction', 'Science', 'Detective', 'Psychology',
];

const Signup: React.FC = () => {
  const [step, setStep] = useState(1);
  const [selectedGenres, setSelectedGenres] = useState<string[]>([]);
  const [stepOneData, setStepOneData] = useState<StepOneInputs | null>(null);
  const [stepTwoData, setStepTwoData] = useState<StepTwoInputs | null>(null);

  const {
    register: registerStepOne,
    handleSubmit: handleSubmitStepOne,
    formState: { errors: errorsStepOne },
  } = useForm<StepOneInputs>({
    resolver: yupResolver(stepOneSchema),
  });

  const {
    register: registerStepTwo,
    handleSubmit: handleSubmitStepTwo,
    formState: { errors: errorsStepTwo },
  } = useForm<StepTwoInputs>({
    resolver: yupResolver(stepTwoSchema),
  });

  const handleStepOneSubmit: SubmitHandler<StepOneInputs> = (data) => {
    console.log(data);
    setStepOneData(data);
    setStep(2);
  };

  const handleStepTwoSubmit: SubmitHandler<StepTwoInputs> = (data) => {
    console.log(data);
    setStepTwoData(data);
    setStep(3);
  };

  const handleFinalSubmit = () => {
    console.log("Step 1 Data: ", stepOneData);
    console.log("Step 2 Data: ", stepTwoData);
    console.log("Selected Genres: ", selectedGenres);
  };

  const handleGenreSelect = (genre: string) => {    
    if (selectedGenres.includes(genre)) {
      setSelectedGenres(selectedGenres.filter((g) => g !== genre));
    } else {
      if (selectedGenres.length < 5) {
        setSelectedGenres([...selectedGenres, genre]);
      }
    }
    console.log(selectedGenres);
  };

  const variants = {
    initial: { opacity: 0, x: -100 },
    animate: { opacity: 1, x: 0 },
    exit: { opacity: 0, x: 100 },
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
          <div className="w-full max-w-md">
            <span className="text-sm text-gray-900">Want An Account? Let's Get Started</span>
            <motion.div
              key={step}
              initial="initial"
              animate="animate"
              exit="exit"
              variants={variants}
              transition={{ duration: 0.5 }}
            >
              {step === 1 && (
                <form onSubmit={handleSubmitStepOne(handleStepOneSubmit)}>
                  <div>
                    <h1 className="text-2xl md:text-3xl font-bold">Sign Up for an Account</h1>
                  </div>
                  <div className="mt-5">
                    <label className="block text-md mb-2" htmlFor="name">
                      Name
                    </label>
                    <input
                      className="px-4 w-full border-2 py-2 rounded-md text-sm outline-none"
                      type="text"
                      {...registerStepOne("name")}
                      placeholder="Name"
                    />
                    {errorsStepOne.name && (
                      <p className="text-red-500 text-sm mt-1">
                        {errorsStepOne.name.message}
                      </p>
                    )}
                  </div>
                  <div className="my-3">
                    <label className="block text-md mb-2" htmlFor="email">
                      Email
                    </label>
                    <input
                      className="px-4 w-full border-2 py-2 rounded-md text-sm outline-none"
                      type="email"
                      {...registerStepOne("email")}
                      placeholder="Email"
                    />
                    {errorsStepOne.email && (
                      <p className="text-red-500 text-sm mt-1">
                        {errorsStepOne.email.message}
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
                      {...registerStepOne("password")}
                      placeholder="Password"
                    />
                    {errorsStepOne.password && (
                      <p className="text-red-500 text-sm mt-1">
                        {errorsStepOne.password.message}
                      </p>
                    )}
                  </div>
                  <button
                    className="mt-4 mb-3 w-full bg-bronze hover:bg-[#a42727] text-white py-2 rounded-md transition duration-100"
                    type="submit"
                  >
                    Next
                  </button>
                </form>
              )}
              {step === 2 && (
                <form onSubmit={handleSubmitStepTwo(handleStepTwoSubmit)}>
                  <div>
                    <h1 className="text-2xl md:text-3xl font-bold">Sign Up</h1>
                  </div>
                  <div className="mt-5">
                    <label className="block text-md mb-2" htmlFor="location">
                      Location
                    </label>
                    <input
                      className="px-4 w-full border-2 py-2 rounded-md text-sm outline-none"
                      type="text"
                      {...registerStepTwo("location")}
                      placeholder="Location"
                    />
                    {errorsStepTwo.location && (
                      <p className="text-red-500 text-sm mt-1">
                        {errorsStepTwo.location.message}
                      </p>
                    )}
                  </div>
                  <div className="my-3">
                    <label className="block text-md mb-2" htmlFor="contact">
                      Contact Number
                    </label>
                    <input
                      className="px-4 w-full border-2 py-2 rounded-md text-sm outline-none"
                      type="text"
                      {...registerStepTwo("contact")}
                      placeholder="Contact Number"
                    />
                    {errorsStepTwo.contact && (
                      <p className="text-red-500 text-sm mt-1">
                        {errorsStepTwo.contact.message}
                      </p>
                    )}
                  </div>
                  <button
                    className="mt-4 mb-3 w-full bg-bronze hover:bg-[#a42727] text-white py-2 rounded-md transition duration-100"
                    type="submit"
                  >
                    Next
                  </button>
                </form>
              )}
              {step === 3 && (
                <div className="flex flex-col items-center w-full">
                  <h1 className="text-2xl md:text-3xl font-bold mb-6 text-left text-nowrap">Select 5 of Your Favorite Genres</h1>
                  <div className="grid grid-cols-5 gap-4 mb-6">
                    {genres.map((genre) => (
                      <div 
                        key={genre} 
                        className={`flex flex-col items-center cursor-pointer ${selectedGenres.includes(genre) ? 'selected' : ''}`} 
                        onClick={() => handleGenreSelect(genre)}
                      >
                        <motion.img
                          src={`/assets/genres/${genre.toLowerCase()}.png`}
                          alt={genre}
                          className="w-16 h-16 object-contain object-center rounded-2xl"
                          whileHover={{ scale: 1.1 }}
                        />
                        <span className="mt-2 text-center">{genre}</span>
                      </div>
                    ))}
                  </div>
                  <button
                    className="mt-4 mb-3 w-full bg-bronze hover:bg-[#a42727] text-white py-2 rounded-md transition duration-100"
                    onClick={handleFinalSubmit}
                  >
                    Complete Signup
                  </button>
                </div>
              )}
            </motion.div>
            {step > 1 && (
              <button
                className="mt-1 mb-3 w-full bg-gray-500 hover:bg-gray-400 text-white py-2 rounded-md transition duration-100"
                onClick={() => setStep(step - 1)}
              >
                Back
              </button>
            )}
          </div>
        </div>
      </div>
    </div>
  );
};

export default Signup;

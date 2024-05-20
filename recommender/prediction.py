import torch
import torch.nn.functional as F
import numpy as np

from utils import (
    CudaUtils, EncoderUtils, RatingsPredictorGMF, RatingsPredictorMLP
)

class Predictor:
    def __init__(self, mod_path, device):
        self.userid_encoder, self.isbn_encoder = EncoderUtils.load_encoders()
        
        mod_n_books = len(self.isbn_encoder.classes_)
        mod_n_users = len(self.userid_encoder.classes_)

        self.model = RatingsPredictorGMF(
                n_books=mod_n_books, 
                n_users=mod_n_users
            ).to(device)
        self.model.load_state_dict(torch.load(mod_path))

        self.average_reader_idx = self.get_average_reader_index()


    def get_average_reader_index(self):
        if type(self.model).__name__ == "RatingsPredictorGMF":
            user_embeddings = self.model.user_embed.weight.data
        else:
            user_embeddings = self.model.user_embed_mlp.weight.data
        
        average_user_embedding = torch.mean(user_embeddings, dim=0)
        cos_sim = F.cosine_similarity(user_embeddings, average_user_embedding.unsqueeze(0))
        average_reader_idx = torch.argmax(cos_sim).item()

        return average_reader_idx


    def predict(self, users, books):
        self.model.eval()
        with torch.no_grad():
            predictions = self.model(users, books)

        return predictions
    

    def recommend_CF(self, user_id, device, top_n=10):
        if user_id not in self.userid_encoder.classes_:
            user_index = self.average_reader_idx
        else:
            user_index = self.userid_encoder.transform([user_id])[0]
    
        user_tensor = torch.tensor([user_index] * len(self.isbn_encoder.classes_), dtype=torch.long).to(device)
        book_tensor = torch.arange(len(self.isbn_encoder.classes_), dtype=torch.long).to(device)
        
        predictions = self.predict(user_tensor, book_tensor)
        
        top_n_books = predictions.view(-1).argsort(descending=True)[:top_n]
        recommended_books = self.isbn_encoder.inverse_transform(top_n_books.to(torch.device('cpu')).numpy())
        
        return recommended_books
    


if __name__ == "__main__":
    device = CudaUtils.get_device()
    predictor = Predictor("./models/matfac_model.pth", device)
    print(predictor.recommend_CF("276737", device, top_n=10))
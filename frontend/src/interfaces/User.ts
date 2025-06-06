export interface User {
    id: number;
    email: string;
    username: string;
    evaluation_rubric?: string | null;
    business_summary?: string | null;
  }
  
export interface UserCreate {
  email: string;
  username: string;
  password: string;
}
  
export interface UserResponse extends User{
  id: number;
  email: string;
  username: string;
  evaluation_rubric?: string 
  business_summary?: string
}
export interface ApiResponse {
    status: string;
    message: string;
    data?: {
        results: any;
    };
    details?: {
        error: string;
        [key: string]: any;
    };
    status_code: number;
}
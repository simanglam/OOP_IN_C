struct Point{
	int x;
	int y;
};

int main(){
    struct Point b = {.x = 2, .y = 4};
    printf("%d", b.x);
}
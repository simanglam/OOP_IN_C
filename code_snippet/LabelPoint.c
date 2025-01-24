struct Point{
	int x;
	int y;
};

struct LabeledPoint{
	int x;
	int y;
	char* label;
};

int calculateDistance(struct Point * a, struct Point * b){
	return 
	sqrt((b->x - a->x) * (b->x - a->x) + (b->y - a->y) * (b->y - a->y));
}

int main(){
	struct Point a = {0, 0};
	struct LabeledPoint b = {3, 4, "My Home"};
	printf("%d", calculateDistance(&a, (struct Point *)&b));
}

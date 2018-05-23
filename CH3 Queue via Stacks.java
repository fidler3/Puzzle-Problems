public class StackQueue{
	Stack insert = new Stack();
	Stack pop = new Stack();

	void push(item a){
		insert.push(a);
	}
	Object pop(){
		if(pop.isEmpty()){
			while(!insert.isEmpty()){
				pop.push(insert.pop());
			}
			return pop.pop();
		}
		return pop.pop();
	}
	
}
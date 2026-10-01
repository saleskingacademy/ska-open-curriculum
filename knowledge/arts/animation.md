---
key: animation
title: "Animation"
program: arts
course_level: 2
dna16: "0701201825963853"
l4_address: "S6:P1118509956"
chain256_anchor: "0252223334941500139398050610581213512453589058120857592758771709116165462220307204536563938358121677920327275812049271071655840707946055925618390262968679645812079869824965581212247316367862910575514246653713021785626803581201590665755158121204510417160232"
updated_at: "2026-10-01T20:00:00.000Z"
license: All-Rights-Reserved (Sales King Academy LLC)
source: Sales King Academy knowledge base (ska_knowledge)
---

# Animation

> The course teaches core principles of animation, including keyframe animation, squash and stretch formula, and timing and spacing matrix.

## Foundations

Animation is the sequential presentation of static images or frames to create the illusion of continuous motion, leveraging the persistence of vision phenomenon in human perception. At its core, animation manipulates time and space by interpolating discrete visual states, typically at frame rates exceeding 12 frames per second (fps) to achieve fluidity. The fundamental principle is the frame-by-frame alteration of visual elements, governed by temporal coherence and spatial transformation, to simulate motion, emotion, or narrative progression. Animation encompasses multiple domains: traditional hand-drawn (cel) animation, stop-motion, computer-generated imagery (CGI), and procedural animation, each relying on core concepts such as keyframing, inbetweening, timing, spacing, squash and stretch, anticipation, and follow-through.

In the arts, animation refers to the process of creating the illusion of motion and change by displaying a sequence of static images, known as frames, in rapid succession. A practitioner of animation, called an animator, must understand the core definitions and first principles of the medium. Key terms include: frame, defined as a single static image within a sequence; frame rate, referring to the speed at which frames are displayed, typically measured in frames per second (fps); and motion, which is the illusion of movement created by the sequential display of frames. The persistence of vision, a phenomenon where the human eye retains an image for a fraction of a second after it has disappeared, is crucial to the animation process, as it allows the brain to fill in the gaps between frames, creating the illusion of continuous motion. Other essential vocabulary includes: keyframe, which is a frame that defines a specific point in an animation, such as the beginning or end of a movement; tweening, the process of creating intermediate frames between keyframes; and squash and stretch, a fundamental principle of animation that refers to the ability of an object to change shape in response to motion or external forces, while maintaining its volume. Understanding these foundational concepts and terms is essential for a practitioner to create effective and engaging animations.

## Keyframe Animation

Keyframe animation is the backbone of both traditional and digital animation workflows. It involves defining critical poses or states (keyframes) at specific points on a timeline, with intermediate frames (inbetweens) generated either manually or algorithmically. The classical approach uses the 12 Principles of Animation (Disney, 1930s), notably timing (number of frames between key poses), spacing (distance between positional changes per frame), and easing (acceleration/deceleration curves). In digital tools (e.g., Autodesk Maya, Adobe After Effects), keyframes are set on property curves, with interpolation methods such as linear, bezier, or stepped determining motion dynamics. For example, a walk cycle typically uses 8 keyframes per cycle at 24 fps, with timing adjusted to convey weight and personality.

## Squash And Stretch Formula

Squash and stretch quantify deformation to convey weight and flexibility, enhancing believability. The volume preservation formula ensures physical plausibility:  
\[ V = A \times L = \text{constant} \]  
where \(A\) is cross-sectional area, \(L\) is length. When an object stretches (increased \(L\)), \(A\) decreases proportionally to maintain constant volume \(V\). For a sphere deforming into an ellipse:  
\[ \pi r^2 \times 2r = \pi a b \times 2c \quad \Rightarrow \quad a b c = r^3 \]  
Animators adjust shape parameters \(a,b,c\) frame-by-frame to simulate elasticity, e.g., a bouncing ball squashes on impact and stretches in ascent/descent phases, typically over 3-5 frames per deformation for smooth perception.

## Timing And Spacing Matrix

Timing (duration of an action) and spacing (distribution of frames) define motion dynamics. The Timing and Spacing Matrix is a 2D framework mapping frame count (timing) on one axis and spatial displacement per frame (spacing) on the other. For example:  
- Slow in/slow out motions use non-linear spacing with frames clustered near start/end (ease-in/ease-out curves).  
- Fast actions have fewer frames with larger spacing, e.g., a punch might use 6 frames at 24 fps with spacing increasing exponentially to peak velocity.  
Quantitatively, spacing \(s_n\) between frames can follow functions such as:  
\[ s_n = s_0 \times e^{k n} \]  
where \(k\) controls acceleration rate, \(n\) frame index. Mastery involves adjusting \(k\) and frame counts to evoke desired physicality and emotion.

## Inverse Kinematics (Ik) System

IK is a computational method for animating articulated figures by specifying end-effector positions, with joint angles computed automatically. The core algorithm solves:  
\[ \mathbf{p} = f(\theta_1, \theta_2, ..., \theta_n) \]  
where \(\mathbf{p}\) is the end-effector position, \(\theta_i\) joint angles. Numerical methods such as Jacobian Inverse or Cyclic Coordinate Descent (CCD) iteratively minimize positional error:  
\[ \min_{\theta} \| \mathbf{p}_{target} - f(\theta) \| \]  
IK enables animators to position hands/feet precisely without manual joint rotation, critical in 3D animation pipelines (Maya, Blender). Typical chain lengths range from 3 to 7 joints for limbs; constraints (joint limits, pole vectors) ensure natural articulation.

## Motion Capture Data Integration

Motion capture (mocap) records real-world movement via sensors or optical markers, producing time-stamped joint rotations or marker positions. Integration involves:  
1. Data cleaning: noise filtering (e.g., Butterworth low-pass filter at 6 Hz cutoff).  
2. Retargeting: mapping mocap skeleton to target rig using joint correspondence matrices and scaling factors.  
3. Blending: combining mocap with keyframe animation via weighted interpolation:  
\[ \theta_{final} = w \theta_{mocap} + (1-w) \theta_{keyframe} \]  
where \(w \in [0,1]\). Mocap provides realistic base motion, while manual tweaks add stylization or correct artifacts.

## Physics-Based Animation

Physics-based animation simulates motion via numerical integration of Newtonian mechanics. The fundamental equation:  
\[ m \frac{d^2 \mathbf{x}}{dt^2} = \mathbf{F} \]  
where \(m\) is mass, \(\mathbf{x}\) position, \(\mathbf{F}\) net force. Common methods include explicit Euler, semi-implicit Euler, and Verlet integration, with timestep \(\Delta t\) typically 1/60 s for real-time stability. Constraints (e.g., joints, collisions) are solved using Lagrange multipliers or penalty methods. Applications include cloth simulation, rigid body dynamics, and soft body deformation, enabling physically plausible secondary motion and interaction.

## Mastery Levels

L1: Understand frame rates and basic flipbook animation principles.  
L2: Apply keyframing with linear interpolation for simple motion.  
L3: Implement squash and stretch preserving volume in bouncing ball exercises.  
L4: Manipulate timing and spacing curves to convey weight and emotion.  
L5: Use inverse kinematics for realistic limb articulation in 3D rigs.  
L6: Integrate and clean motion capture data for hybrid animation workflows.  
L7: Develop physics-based simulations for secondary motion and environmental interaction.  
L8: Innovate procedural animation algorithms combining AI, physics, and artistic intent for autonomous, emotionally resonant character performances.

## Mechanisms

The process of creating animation involves a series of steps that work together to create the illusion of movement. It begins with pre-production, where the concept, script, and storyboard are developed. The storyboard is a visual representation of the sequence of events, broken down into individual shots or frames. Next, the assets, such as characters, backgrounds, and props, are designed and created. These assets are then brought to life through keyframe animation, where the animator sets specific poses or positions for the assets at specific points in time. The computer or software then fills in the missing frames, creating the illusion of movement through a process called tweening. The animation is then refined through the addition of timing, spacing, and motion, with attention to the principles of animation, such as squash and stretch, anticipation, and follow-through. The final step is post-production, where the animation is edited, sound effects and music are added, and the final product is rendered. Throughout this process, the animator must consider the 12 basic principles of animation, which include principles such as exaggeration, staging, and appeal, to create a believable and engaging animation. The causal chain is as follows: the creation of assets and keyframe animation leads to the generation of in-between frames, which in turn creates the illusion of movement, and ultimately, the final animated product.

## Methods And Frameworks

In animation, several methods and frameworks are employed to create the illusion of movement. The 12 Basic Principles of Animation, developed by Disney animators Ollie Johnston and Frank Thomas, provide a foundation for creating believable and engaging animations. These principles include squash and stretch, anticipation, staging, straight ahead action, and follow through, among others. The key to using these principles effectively is to understand when to apply each one, such as using squash and stretch to create a sense of weight and flexibility in a character's movements. 
The walk cycle, a fundamental framework in animation, involves breaking down the movement of a character walking into its component parts, including the contact position, down position, passing position, and up position. This framework is useful for creating repetitive movements, but can fail if not varied to create a sense of naturalism. 
The pose-to-pose method involves creating key frames, or specific poses, and then filling in the missing frames to create the illusion of movement. This method is useful for creating complex, nuanced movements, but can fail if the key frames are not well-defined or if the spacing between them is not consistent. 
The straight ahead method, on the other hand, involves creating each frame in sequence, without planning out the entire animation in advance. This method is useful for creating spontaneous, dynamic movements, but can fail if the animation becomes too chaotic or difficult to control. 
Understanding the strengths and limitations of each method and framework is crucial for creating effective animations that engage and captivate the audience. The keyframe animation method involves setting specific frames and allowing the computer to fill in the missing frames, useful for complex scenes and character movements. The tweening method, used in computer-generated imagery (CGI), involves specifying the start and end points of a movement and allowing the software to generate the intermediate frames. The stop-motion method, used in traditional animation, involves physically manipulating objects and capturing each frame individually. The failure mode of these methods often lies in inconsistent timing, lack of anticipation, and poor staging, resulting in animations that appear stiff or unconvincing. The use of formulas, such as the equation of motion and kinematic equations, can help animators create more realistic movements and interactions. Understanding the principles of motion, such as acceleration, velocity, and friction, is crucial for creating believable animations. By applying these methods and frameworks, animators can create engaging and realistic animations that capture the viewer's attention.

## Worked Examples

To illustrate key concepts in animation, consider the following examples. 
1. A character's arm is animated to move from a 90-degree angle to a 180-degree angle over 24 frames. If the animator wants the arm to accelerate uniformly, the angle of the arm at frame 12 can be calculated using the equation of motion: θ = θ0 + ω0t + 0.5αt^2, where θ is the final angle, θ0 is the initial angle, ω0 is the initial angular velocity (0, since it starts from rest), α is the angular acceleration, and t is time. Since the arm accelerates uniformly, the angular displacement is 90 degrees over 24 frames, so the angular acceleration α can be calculated as 90 degrees / (0.5 * 24^2) = 0.078 degrees/frame^2. At frame 12, t = 12, so θ = 90 + 0 + 0.5 * 0.078 * 12^2 = 112.5 degrees.
2. A ball is animated to bounce off the ground, with an initial velocity of 10 pixels/frame and a restitution coefficient of 0.7. If the ball takes 30 frames to reach the ground, its velocity at frame 20 can be calculated using the equation v = v0 - gt, where v is the final velocity, v0 is the initial velocity, g is the acceleration due to gravity (approximately 0.5 pixels/frame^2), and t is time. At frame 20, t = 20, so v = 10 - 0.5 * 20 = 0 pixels/frame, indicating that the ball has come to a temporary stop. After the bounce, the ball's velocity will be -0.7 * 10 = -7 pixels/frame.
3. A walk cycle is animated at 30 frames per second, with the character's leg taking 1.2 seconds to complete one cycle. To calculate the number of frames required for one cycle, the equation frames = time * fps can be used, where frames is the number of frames, time is the time taken, and fps is the frames per second. So, frames = 1.2 * 30 = 36 frames. If the animator wants the leg to be in the air for 40% of the cycle, the number of frames the leg is in the air can be calculated as 0.4 * 36 = 14.4 frames. **Frame Rate Calculation**: An animator is working on a 2D animation project with a desired frame rate of 24 frames per second (fps). If the animation is 5 minutes long, how many frames will it contain? First, convert the length of the animation to seconds: 5 minutes * 60 seconds/minute = 300 seconds. Then, calculate the total number of frames: 300 seconds * 24 fps = 7200 frames.
2. **Walk Cycle Analysis**: A character's walk cycle consists of 8 key frames. If the walk cycle is to be completed in 0.8 seconds and the animation is running at 30 fps, how many frames will each key frame occupy? First, calculate the total number of frames in the walk cycle: 0.8 seconds * 30 fps = 24 frames. Then, divide the total frames by the number of key frames to find the occupancy of each: 24 frames / 8 key frames = 3 frames per key frame.
3. **Animation Timing**: An animator wants to create a scene where a ball falls from the top of the screen to the bottom over a period of 4 seconds. If the animation is running at 25 fps, how many frames will the ball be falling? First, calculate the total number of frames: 4 seconds * 25 fps = 100 frames. To create a sense of acceleration, the animator can use fewer frames at the start and more towards the end, applying the principle of easing to simulate real-world physics.

## Applications

In the arts, animation has numerous applications across various mediums and industries. One of the primary applications is in film and television production, where animation is used to create special effects, title sequences, and entire animated films. For instance, traditional animation techniques, such as hand-drawn animation and stop-motion, are used to create unique visual styles and storytelling methods. Computer-generated imagery (CGI) is also widely used in modern animation, allowing for greater control and precision in creating complex characters, environments, and effects. 
In addition to film and television, animation is also used in video game production, where it is used to create characters, cutscenes, and gameplay mechanics. The principles of animation, such as the 12 basic principles of animation, are applied to create believable and engaging character movements and interactions. 
Animation is also used in advertising, where it is used to create eye-catching and memorable commercials, as well as in educational settings, where it is used to create interactive and engaging learning materials. Furthermore, animation is used in fine arts, where artists use animation as a medium to create experimental and avant-garde works, pushing the boundaries of the medium and exploring new ways of storytelling and visual expression. 
The application of animation in different domains requires a deep understanding of the principles of animation, as well as the technical skills to bring those principles to life. By applying the principles of animation, artists and animators can create a wide range of content, from realistic simulations to stylized and fantastical worlds, and engage audiences in new and innovative ways. Furthermore, animation is used in advertising, where it is used to create eye-catching commercials, logos, and brand identities. The use of animation in advertising allows companies to convey complex information in a simple and engaging manner, making it an effective tool for marketing and branding. Animation is also used in fine arts, where it is used to create experimental and avant-garde films, installations, and performances. Artists use animation to push the boundaries of traditional art forms, exploring new ways to express themselves and engage with audiences. Overall, the applications of animation in the arts are diverse and widespread, and its use continues to evolve and expand into new areas, such as virtual reality, augmented reality, and online media.

## Common Errors

In the field of animation, practitioners often make mistakes that can detract from the overall quality and believability of their work. One common error is the misuse of squash and stretch principles, where animators exaggerate or distort characters' movements without maintaining a consistent volume, leading to a loss of realism. Another mistake is the failure to properly anticipate and follow through with actions, resulting in movements that appear stiff or unnatural. Additionally, animators may neglect to consider the principles of timing and spacing, leading to pacing issues and a lack of visual flow. The misuse of easing, such as abrupt acceleration or deceleration, can also disrupt the fluidity of motion. Furthermore, ignoring the fundamental principles of animation, such as the 12 basic principles outlined by the Disney animators Ollie Johnston and Frank Thomas, can result in animations that lack depth, emotion, and engagement. These principles, including squash and stretch, anticipation, staging, and secondary action, provide a foundation for creating believable and engaging animations. By understanding and avoiding these common errors, animators can create more polished and effective animations that capture the viewer's attention and convey the intended message.

## Advanced

At the graduate level, animation studies delve into specialized areas such as experimental animation, hybrid practices, and interdisciplinary collaborations. Students explore the intersection of animation with other art forms like dance, theater, and visual effects. The concept of "expanded animation" emerges, which encompasses a broad range of techniques, including stop-motion, 3D printing, and virtual reality. Researchers investigate the potential of animation to convey complex ideas and emotions, pushing the boundaries of narrative storytelling. Open questions in the field include the role of animation in social commentary, the impact of technology on traditional techniques, and the relationship between animation and cognitive psychology. The field is moving towards increased experimentation with new technologies, such as motion capture and artificial intelligence, and a growing recognition of animation as a distinct art form with its own history, theory, and criticism. Graduate-level studies also focus on the preservation and restoration of animated films, as well as the development of new methodologies for analyzing and interpreting animated texts. Furthermore, the rise of independent animation and online platforms has democratized the field, allowing for a more diverse range of voices and styles to emerge. As a result, graduate-level animation studies must consider the global and cultural contexts of animation production and reception, highlighting the need for a more nuanced understanding of the complex relationships between animation, culture, and society. Researchers are also investigating the application of animation principles to non-traditional areas, like data visualization, scientific simulation, and architectural design. Furthermore, the increasing accessibility of animation tools and software has democratized the medium, raising questions about authorship, ownership, and the future of animation as a collaborative and global practice. As the field continues to evolve, graduate-level studies in animation are poised to push the boundaries of the medium, exploring new modes of storytelling, new technologies, and new ways of thinking about the relationship between animation, art, and society.
